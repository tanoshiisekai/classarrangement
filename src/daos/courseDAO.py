from dbmodels.courseDBModel import Course
from dbmodels.coursegroupDBModel import CourseGroup
from dbmodels.classDBModel import Class1
from appbase import global_db as gdb
from tools.packtools import packinfo, packjoinquery
from sqlalchemy import and_, or_
from tools.log import logger


class CourseDAO:

    @staticmethod
    def getallcoursedetails():
        clist = gdb.session.query(Course).all()
        try:
            clist = [x.todict() for x in clist]
            clist = [CourseDAO.addcourseclasslistdetails(x) for x in clist]
        except Exception as e:
            return packinfo(infostatus=False, infomsg="课程查询失败！不存在的数据或数据库错误！")
        else:
            return packinfo(infostatus=True, infomsg="课程查询成功！", inforesult=clist)

    @staticmethod
    def getcoursedetailsbyid(courseid):
        cou = gdb.session.query(Course).filter(Course.course_id==courseid).first()
        try:
            cou = cou.todict()
            cou = CourseDAO.addcourseclasslistdetails(cou)
        except Exception as e:
            return packinfo(infostatus=False, infomsg="课程查询失败！不存在的数据或数据库错误！")
        else:
            return packinfo(infostatus=True, infomsg="课程查询成功！", inforesult=cou)

    @staticmethod
    def addcourseclasslistdetails(xdict):
        if xdict["course_isgroup"]:
            classlist = gdb.session.query(CourseGroup, Class1).filter(
                CourseGroup.course_id == xdict["course_id"]
            ).filter(
                CourseGroup.class_id == Class1.class_id
            ).all()
            classlist = [x[1] for x in classlist]
            classlist = [x.class_name for x in classlist]
            classliststr = ",".join(classlist)
            xdict.update({"course_classlist": classliststr})
        else:
            xdict.update({"course_classlist": ""})
        return xdict

    @staticmethod
    def addcourseclasslist(xdict):
        if xdict["course_isgroup"]:
            classlist = gdb.session.query(CourseGroup.class_id).filter(
                CourseGroup.course_id == xdict["course_id"]
            ).all()
            classlist = [str(x[0]) for x in classlist]
            classliststr = ",".join(classlist)
            xdict.update({"course_classlist": classliststr})
        else:
            xdict.update({"course_classlist": ""})
        return xdict

    @staticmethod
    def getallcourse():
        clist = gdb.session.query(Course).all()
        try:
            clist = [x.todict() for x in clist]
            clist = [CourseDAO.addcourseclasslist(x) for x in clist]
        except Exception as e:
            return packinfo(infostatus=False, infomsg="课程查询失败！不存在的数据或数据库错误！")
        else:
            return packinfo(infostatus=True, infomsg="课程查询成功！", inforesult=clist)

    @staticmethod
    def getcoursebyid(courseid):
        cou = gdb.session.query(Course).filter(Course.course_id==courseid).first()
        try:
            cou = cou.todict()
            cou = CourseDAO.addcourseclasslist(cou)
        except Exception as e:
            return packinfo(infostatus=False, infomsg="课程查询失败！不存在的数据或数据库错误！")
        else:
            return packinfo(infostatus=True, infomsg="课程查询成功！", inforesult=cou)

    @staticmethod
    def addcourse(params):
        cou = params
        course_name = cou["course_name"]
        course_isgroup = cou["course_isgroup"]
        if course_isgroup:
            course_list = cou["course_classlist"].split(",")
            cour = Course(course_name, course_isgroup)
            try:
                gdb.session.add(cour)
                gdb.session.commit()
            except Exception as e:
                return packinfo(infostatus=False, infomsg="数据库错误1！数据添加失败！")
            else:
                coid = gdb.session.query(Course).filter(
                    and_(Course.course_name == course_name,
                         Course.course_isgroup == course_isgroup)).first().course_id
                if coid:
                    for cl in course_list:
                        cg = CourseGroup(coid, int(cl))
                        gdb.session.add(cg)
                    try:
                        gdb.session.commit()
                    except Exception as e:
                        return packinfo(infostatus=False, infomsg="数据库错误2！数据添加失败！")
                    else:
                        return packinfo(infostatus=True, infomsg="合班课程添加成功！")
                else:
                    return packinfo(infostatus=False, infomsg="数据库错误3！数据添加失败！")

        else:
            course_list = ""
            cour = Course(course_name, course_isgroup)
            try:
                gdb.session.add(cour)
                gdb.session.commit()
            except Exception as e:
                return packinfo(infostatus=False, infomsg="数据库错误4！数据添加失败！")
            else:
                return packinfo(infostatus=True, infomsg="非合班课程添加成功！")

    @staticmethod
    def removecourse(courseid):
        cou = gdb.session.query(Course).filter(Course.course_id==courseid).first()
        if cou.course_isgroup:
            subcoulist = gdb.session.query(CourseGroup).filter(CourseGroup.course_id==courseid).all()
            for sc in subcoulist:
                try:
                    gdb.session.delete(sc)
                    gdb.session.commit()
                except Exception as e:
                    return packinfo(infostatus=False, infomsg="课程删除失败！不存在的数据或数据库错误！")
        try:
            gdb.session.delete(cou)
            gdb.session.commit()
        except Exception as e:
            return packinfo(infostatus=False, infomsg="课程删除失败！不存在的数据或数据库错误！")
        else:
            return packinfo(infostatus=True, infomsg="课程删除成功！")

