from dbmodels.arrangementDBModel import Arrangement
from dbmodels.classDBModel import Class1
from dbmodels.courseDBModel import Course
from dbmodels.classroomDBModel import Classroom
from dbmodels.courseplanDBModel import CoursePlan
from dbmodels.coursegroupDBModel import CourseGroup
from appbase import global_db as gdb
from tools.packtools import packinfo, packjoinquery
from sqlalchemy import and_
from tools.businesstools import checknullvalue, availabletimetodict


class ArrangementDAO:

    @staticmethod
    def checkcoursetime(classid, week, section):
        temp = gdb.session.query(Arrangement).filter(and_(
            Arrangement.class_id == classid,
            Arrangement.arrangement_week == week,
            Arrangement.arrangement_section == section
        )).first()
        if temp:
            otherclass = gdb.session.query(Class1).filter(
                Class1.class_id == temp.class_id
            ).first().class_name
            othercourse = gdb.session.query(Course).filter(
                Course.course_id == temp.course_id
            ).first().course_name
            return (otherclass, othercourse)
        else:
            return False

    @staticmethod
    def checkteacher(teacherid, week, section):
        temp = gdb.session.query(Arrangement).filter(and_(
            Arrangement.teacher_id == teacherid,
            Arrangement.arrangement_week == week,
            Arrangement.arrangement_section == section
        )).first()
        if temp:
            otherclass = gdb.session.query(Class1).filter(
                Class1.class_id == temp.class_id
            ).first().class_name
            othercourse = gdb.session.query(Course).filter(
                Course.course_id == temp.course_id
            ).first().course_name
            return (otherclass, othercourse)
        else:
            return False

    @staticmethod
    def checkclassroom(classroomid, week, section):
        temp = gdb.session.query(Arrangement).filter(and_(
            Arrangement.classroom_id == classroomid,
            Arrangement.arrangement_week == week,
            Arrangement.arrangement_section == section
        )).first()
        if temp:
            otherclass = gdb.session.query(Class1).filter(
                Class1.class_id == temp.class_id
            ).first().class_name
            othercourse = gdb.session.query(Course).filter(
                Course.course_id == temp.course_id
            ).first().course_name
            return (otherclass, othercourse)
        else:
            return False

    @staticmethod
    def removearrangement(classid, courseid):
        """
        删除排课
        """
        isgroup = gdb.session.query(Course.course_isgroup).filter(
            Course.course_id == courseid).first()
        removelist = []
        if isgroup:
            if isgroup[0] == 1:
                # 处理合班课
                classidlist = gdb.session.query(CoursePlan.class_id).filter(
                    CoursePlan.course_id == courseid).all()
                classidlist = [x[0] for x in classidlist]
                for cid in classidlist:
                    removelist.append({"class_id": cid, "course_id": courseid})
            else:
                # 处理非合班课
                removelist.append({"class_id": classid, "course_id": courseid})
            for rl in removelist:
                arrlist = gdb.session.query(Arrangement).filter(and_(
                    Arrangement.class_id == rl["class_id"],
                    Arrangement.course_id == rl["course_id"]
                )).all()
                for ar in arrlist:
                    gdb.session.delete(ar)
            try:
                gdb.session.commit()
            except Exception as e:
                return packinfo(infostatus=False, infomsg="数据库错误！排课删除失败！")
            else:
                return packinfo(infostatus=True, infomsg="排课删除成功！")
        else:
            return packinfo(infostatus=False, infomsg="课程编号有误！排课删除失败！")

    @staticmethod
    def changearrangement(class1id, week1, section1, class2id, week2, section2):
        """
        调课
        """
        print(class1id)
        print(class2id)
        print(week1)
        print(week2)
        print(section1)
        print(section2)
        arr1 = gdb.session.query(Arrangement).filter(and_(
            Arrangement.class_id == class1id,
            Arrangement.arrangement_week == week1,
            Arrangement.arrangement_section == section1
        )).first()
        arr2 = gdb.session.query(Arrangement).filter(and_(
            Arrangement.class_id == class2id,
            Arrangement.arrangement_week == week2,
            Arrangement.arrangement_section == section2
        )).first()
        if gdb.session.query(Course.course_isgroup).filter(
            Course.course_id == arr1.course_id
        ).first()[0] == 1:
            return packinfo(infostatus=False, infomsg="合班课涉及变动的幅度较大，为保证数据安全，暂不支持调整合班课。")
        if gdb.session.query(Course.course_isgroup).filter(
            Course.course_id == arr2.course_id
        ).first()[0] == 1:
            return packinfo(infostatus=False, infomsg="合班课涉及变动的幅度较大，为保证数据安全，暂不支持调整合班课。")
        # 非合班课
        try:
            arr1.class_id = class2id
            arr1.arrangement_week = week2
            arr1.arrangement_section = section2
            arr2.class_id = class1id
            arr2.arrangement_week = week1
            arr2.arrangement_section = section1
            gdb.session.commit()
        except Exception as e:
            return packinfo(infostatus=False, infomsg="数据库错误！调课失败！")
        return packinfo(infostatus=True, infomsg="调课成功")


    @staticmethod
    def addarrangement(params):
        """
        添加排课
        """
        arr = params
        classid = arr["class_id"]
        courseid = arr["course_id"]
        classroomid = arr["classroom_id"]
        coursetime = arr["coursetime"]
        ignoreclassroom = arr["ignoreclassroom"]
        ignoreteacher = arr["ignoreteacher"]
        ignorecoursetime = arr["ignorecoursetime"]
        teacherid = gdb.session.query(CoursePlan).filter(and_(
            CoursePlan.class_id == classid,
            CoursePlan.course_id == courseid
        )).first().teacher_id
        newcousetime = availabletimetodict(coursetime)
        insertlist = []
        # 处理合班课
        isgroup = gdb.session.query(Course.course_isgroup).filter(
            Course.course_id == courseid).first()
        if isgroup:
            if isgroup[0] == 1:
                classidlist = gdb.session.query(CourseGroup.class_id).filter(
                    CourseGroup.course_id == courseid).all()
                classidlist = [x[0] for x in classidlist]
                for cid in classidlist:
                    for k, v in newcousetime.items():
                        for iv in v:
                            insertlist.append({"classid": cid, "courseid": courseid, "classroomid": classroomid,
                                               "teacherid": teacherid,
                                               "arrangement_week": k, "arrangement_section": iv})
            else:
                for k, v in newcousetime.items():
                    for iv in v:
                        insertlist.append({"classid": classid, "courseid": courseid, "classroomid": classroomid,
                                           "teacherid": teacherid,
                                           "arrangement_week": k, "arrangement_section": iv})
            if int(ignorecoursetime) == 0:
                for il in insertlist:
                    temp = ArrangementDAO.checkcoursetime(
                        il["classid"], il["arrangement_week"], il["arrangement_section"])
                    if temp != False:
                        return packinfo(infostatus=False, infomsg="添加失败！当前添加的课程与　" + temp[0] + "　的　" + temp[1] + "　课在时间上发生冲突！")
            if int(ignoreclassroom) == 0:
                for il in insertlist:
                    temp = ArrangementDAO.checkclassroom(
                        il["classroomid"], il["arrangement_week"], il["arrangement_section"])
                    if temp != False:
                        return packinfo(infostatus=False, infomsg="添加失败！当前添加的课程与　" + temp[0] + "　的　" + temp[1] + "　课在教室上发生冲突！")
            if int(ignoreteacher) == 0:
                for il in insertlist:
                    temp = ArrangementDAO.checkteacher(
                        il["teacherid"], il["arrangement_week"], il["arrangement_section"])
                    if temp != False:
                        return packinfo(infostatus=False, infomsg="添加失败！当前添加的课程与　" + temp[0] + "　的　" + temp[1] + "　课在任课教师上发生冲突！")
            for il in insertlist:
                ar = Arrangement(il["classid"], il["courseid"], il["classroomid"],
                                 il["teacherid"], il["arrangement_week"], il["arrangement_section"])
                gdb.session.add(ar)
            try:
                gdb.session.commit()
            except Exception as e:
                return packinfo(infostatus=False, infomsg="数据库错误！排课失败！")
            else:
                return packinfo(infostatus=True, infomsg="排课成功！")
        else:
            return packinfo(infostatus=False, infomsg="课程编号有误！排课失败！")
