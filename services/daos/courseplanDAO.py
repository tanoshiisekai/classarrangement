from dbmodels.courseplanDBModel import CoursePlan
from dbmodels.courseDBModel import Course
from dbmodels.coursegroupDBModel import CourseGroup
from dbmodels.classDBModel import Class1
from dbmodels.teacherDBModel import Teacher
from daos.courseDAO import CourseDAO
from appbase import global_db as gdb
from tools.packtools import packinfo, packjoinquery
from tools.businesstools import checknullvalue
from sqlalchemy import and_


class CoursePlanDAO:

    @staticmethod
    def getallcourseplandetails():
        """
        返回所有分课时详情
        """
        try:
            coulist = gdb.session.query(CoursePlan, Course, Class1, Teacher).filter(
                CoursePlan.class_id == Class1.class_id).filter(
                    CoursePlan.course_id == Course.course_id).filter(
                        CoursePlan.teacher_id == Teacher.teacher_id
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
        if checknullvalue(class_id, course_id, courseplan_count):
            return packinfo(infostatus=False, infomsg="提交的参数不全！")
        isgroupclass = gdb.session.query(Course.course_isgroup).filter(
            Course.course_id == course_id
        ).first()[0]
        if isgroupclass == 1:
            # 合班课
            groupclasses = gdb.session.query(CourseGroup.class_id).filter(
                CourseGroup.course_id == course_id
            ).all()
            groupclasses = [x[0] for x in groupclasses]
            for ci in groupclasses:
                cpl = CoursePlan(class_id=ci, course_id=course_id,
                                 teacher_id=teacher_id, courseplan_count=courseplan_count)
                if not gdb.session.query(CoursePlan).filter(and_(
                    CoursePlan.class_id == ci, CoursePlan.course_id == course_id,
                    CoursePlan.teacher_id == teacher_id, CoursePlan.courseplan_count == courseplan_count
                )).first():
                    gdb.session.add(cpl)
            try:
                gdb.session.commit()
            except Exception as e:
                return packinfo(infostatus=False, infomsg="数据库错误！分课时添加失败！")
            else:
                return packinfo(infostatus=True, infomsg="分课时添加成功！")
        else:
            # 非合班课
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

    @staticmethod
    def updatecourseplan(courseplanid, params):
        """
        更新分课时
        """
        courseplan = params
        class_id = courseplan["class_id"]
        course_id = courseplan["course_id"]
        teacher_id = courseplan["teacher_id"]
        courseplan_count = courseplan["courseplan_count"]
        if checknullvalue(class_id, course_id, courseplan_count):
            return packinfo(infostatus=False, infomsg="提交的参数不全！")
        cp = gdb.session.query(CoursePlan).filter(
            CoursePlan.courseplan_id == courseplanid).first()
        if cp:
            try:
                cp.class_id = class_id
                cp.course_id = course_id
                cp.teacher_id = teacher_id
                cp.courseplan_count = courseplan_count
                gdb.session.commit()
            except Exception as e:
                return packinfo(infostatus=False, infomsg="数据库错误！分课时更新失败！")
            else:
                return packinfo(infostatus=True, infomsg="分课时更新成功！")
        else:
            return packinfo(infostatus=False, infomsg="分课时编号不存在！分课时更新失败！")
