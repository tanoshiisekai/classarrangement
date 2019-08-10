from dbmodels.arrangementDBModel import Arrangement
from dbmodels.classDBModel import Class1
from dbmodels.courseDBModel import Course
from dbmodels.classroomDBModel import Classroom
from dbmodels.courseplanDBModel import CoursePlan
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
        for k, v in newcousetime.items():
            for iv in v:
                insertlist.append({"classid": classid, "courseid": courseid, "classroomid": classroomid,
                "teacherid": teacherid,
                "arrangement_week": k, "arrangement_section": iv})
        if int(ignorecoursetime) == 0:
            for il in insertlist:
                temp = ArrangementDAO.checkcoursetime(il["classid"], il["arrangement_week"], il["arrangement_section"])
                if temp != False:
                    return packinfo(infostatus=False, infomsg="添加失败！当前添加的课程与　" + temp[0] + "　的　" + temp[1] + "　课在时间上发生冲突！")
        if int(ignoreclassroom) == 0:
            for il in insertlist:
                temp = ArrangementDAO.checkclassroom(il["classroomid"], il["arrangement_week"], il["arrangement_section"])
                if temp != False:
                    return packinfo(infostatus=False, infomsg="添加失败！当前添加的课程与　" + temp[0] + "　的　" + temp[1] + "　课在教室上发生冲突！")
        if int(ignoreteacher) == 0:
            for il in insertlist:
                temp = ArrangementDAO.checkteacher(il["teacherid"], il["arrangement_week"], il["arrangement_section"])
                if temp != False:
                    return packinfo(infostatus=False, infomsg="添加失败！当前添加的课程与　" + temp[0] + "　的　" + temp[1] + "　课在任课教师上发生冲突！")
        for il in insertlist:
            ar = Arrangement(il["classid"], il["courseid"], il["classroomid"], il["teacherid"], il["arrangement_week"], il["arrangement_section"])
            gdb.session.add(ar)
        try:
            gdb.session.commit()
        except Exception as e:
            return packinfo(infostatus=False, infomsg="数据库错误！排课失败！")
        else:
            return packinfo(infostatus=True, infomsg="排课成功！")
