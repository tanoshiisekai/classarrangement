from dbmodels.teacherDBModel import Teacher
from dbmodels.classDBModel import Class1
from dbmodels.courseplanDBModel import CoursePlan
from appbase import global_db as gdb
from tools.packtools import packinfo
from tools.businesstools import checkavailable


class TeacherDAO:

    def getteacherbyid(teacherid):
        """
        根据教师编号查询教师
        """
        try:
            tea = gdb.session.query(Teacher).filter(
                Teacher.teacher_id == teacherid).first()
            tea = tea.todict()
        except Exception as e:
            return packinfo(infostatus=False, infomsg="数据库无数据或发生错误！查询失败！")
        else:
            return packinfo(infostatus=True, inforesult=tea, infomsg="查询成功！")

    @staticmethod
    def getallteacher():
        """
        返回所有教师
        """
        try:
            tealist = gdb.session.query(Teacher).all()
            tealist = [x.todict() for x in tealist]
        except Exception as e:
            return packinfo(infostatus=False, infomsg="数据库无数据或发生错误！查询失败！")
        else:
            return packinfo(infostatus=True, inforesult=tealist, infomsg="查询成功！")

    @staticmethod
    def addteacher(params):
        """
        添加教师
        """
        teacher = params
        teacher_name = teacher["teacher_name"]
        teacher_mobile = teacher["teacher_mobile"]
        teacher_request = teacher["teacher_request"]
        tea = Teacher(teacher_name=teacher_name, teacher_mobile=teacher_mobile,
                      teacher_request=teacher_request)
        try:
            gdb.session.add(tea)
            gdb.session.commit()
        except Exception as e:
            return packinfo(infostatus=False, infomsg="数据库错误！教师添加失败！")
        else:
            return packinfo(infostatus=True, infomsg="教师添加成功！")

    @staticmethod
    def removeteacher(teacherid):
        """
        删除教师
        """
        tea = gdb.session.query(Teacher).filter(
            Teacher.teacher_id == teacherid).first()
        if tea:
            foreigns = gdb.session.query(Class1).filter(
                Class1.teacher_id == teacherid).first()
            if foreigns:
                return packinfo(infostatus=False, infomsg="该教师信息正在被班级管理使用，为保证数据一致性，不可删除！")
            foreigns = gdb.session.query(CoursePlan).filter(
                CoursePlan.teacher_id == teacherid).first()
            if foreigns:
                return packinfo(infostatus=False, infomsg="该教师信息正在被分课时管理使用，为保证数据一致性，不可删除！")
            try:
                gdb.session.delete(tea)
                gdb.session.commit()
            except Exception as e:
                return packinfo(infostatus=False, infomsg="数据库错误！教师删除失败！")
            else:
                return packinfo(infostatus=True, infomsg="教师删除成功！")
        else:
            return packinfo(infostatus=False, infomsg="教师编号不存在！教师删除失败！")

    @staticmethod
    def checkavailabletime(teacherid, week, section):
        """
        判断某一天某一节该老师是否可以上课
        """
        tea = gdb.session.query(Teacher).filter(
            Teacher.teacher_id == teacherid).first()
        if tea:
            if checkavailable(tea.teacher_request, week, section):
                return packinfo(infostatus=True, infomsg="教师该时间段可上课！")
            else:
                return packinfo(infostatus=False, infomsg="教师该时间段不可上课！")
        else:
            return packinfo(infostatus=False, infomsg="教师编号不存在！")

    @staticmethod
    def updateteacher(teacherid, params):
        """
        更新教师
        """
        teacher = params
        teacher_name = teacher["teacher_name"]
        teacher_mobile = teacher["teacher_mobile"]
        teacher_request = teacher["teacher_request"]
        tea = gdb.session.query(Teacher).filter(
            Teacher.teacher_id == teacherid).first()
        if tea:
            try:
                tea.teacher_name = teacher_name
                tea.teacher_mobile = teacher_mobile
                tea.teacher_request = teacher_request
                gdb.session.commit()
            except Exception as e:
                return packinfo(infostatus=False, infomsg="数据库错误！教师更新失败！")
            else:
                return packinfo(infostatus=True, infomsg="教师更新成功！")
        else:
            return packinfo(infostatus=False, infomsg="教师编号不存在！教师更新失败！")
