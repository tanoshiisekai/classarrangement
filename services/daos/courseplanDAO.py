from dbmodels.courseplanDBModel import CoursePlan
from dbmodels.courseDBModel import Course
from dbmodels.classDBModel import Class1
from dbmodels.teacherDBModel import Teacher
from daos.courseDAO import CourseDAO
from appbase import global_db as gdb
from tools.packtools import packinfo, packjoinquery


class CoursePlanDAO:

    @staticmethod
    def getallcourseplandetails():
        """
        返回所有分课时详情
        """
        try:
            coulist = gdb.session.query(CoursePlan, Course, Class1, Teacher).filter(
                CoursePlan.class_id==Class1.class_id).filter(
                    CoursePlan.course_id==Course.course_id).filter(
                        CoursePlan.teacher_id==Teacher.teacher_id
                    ).all()
            coulist = [packjoinquery(x) for x in coulist]
            coulist = [CourseDAO.addcourseclasslistdetails(x) for x in coulist]
        except Exception as e:
            return packinfo(infostatus=False, infomsg="数据库无数据或发生错误！查询失败！")
        else:
            return packinfo(infostatus=True, inforesult=coulist, infomsg="查询成功！")

    @staticmethod
    def getallcourseplan():
        """
        返回所有分课时
        """
        try:
            coulist = gdb.session.query(CoursePlan).all()
            coulist = [x.todict() for x in coulist]
        except Exception as e:
            return packinfo(infostatus=False, infomsg="数据库无数据或发生错误！查询失败！")
        else:
            return packinfo(infostatus=True, inforesult=coulist, infomsg="查询成功！")

    @staticmethod
    def addcourseplan(param):
        """
        添加分课时
        """
        cp = param
        class_id = param["class_id"]
        course_id = param["course_id"]
        teacher_id = param["teacher_id"]
        courseplan_count = param["courseplan_count"]
        cpl = CoursePlan(class_id=class_id, course_id=course_id,
                         teacher_id=teacher_id, courseplan_count=courseplan_count)
        try:
            gdb.session.add(cpl)
            gdb.session.commit()
        except Exception as e:
            return packinfo(infostatus=False, infomsg="数据库错误！分课时添加失败！")
        else:
            return packinfo(infostatus=True, infomsg="分课时添加成功！")
            
    @staticmethod
    def removecourseplan(courseplanid):
        """
        删除分课时
        """
        cou = gdb.session.query(CoursePlan).filter(
            CoursePlan.courseplan_id == courseplanid).first()
        if cou:
            try:
                gdb.session.delete(cou)
                gdb.session.commit()
            except Exception as e:
                return packinfo(infostatus=False, infomsg="数据库错误！分课时删除失败！")
            else:
                return packinfo(infostatus=True, infomsg="分课时删除成功！")
        else:
            return packinfo(infostatus=False, infomsg="分课时编号不存在！分课时删除失败！")