from dbmodels.classroomDBModel import Classroom
from dbmodels.classDBModel import Class1
from dbmodels.arrangementDBModel import Arrangement
from appbase import global_db as gdb
from tools.packtools import packinfo
from tools.businesstools import checkavailable


class ClassroomDAO:

    @staticmethod
    def getclassroombyid(classroomid):
        """
        根据教室编号查询教室
        """
        try:
            cr = gdb.session.query(Classroom).filter(Classroom.classroom_id==classroomid).first()
            cr = cr.todict()
        except Exception as e:
            return packinfo(infostatus=False, infomsg="数据库无数据或发生错误！查询失败！")
        else:
            return packinfo(infostatus=True, inforesult=cr, infomsg="查询成功！")

    @staticmethod
    def getallclassroom():
        """
        返回所有教室
        """
        try:
            crlist = gdb.session.query(Classroom).all()
            crlist = [x.todict() for x in crlist]
        except Exception as e:
            return packinfo(infostatus=False, infomsg="数据库无数据或发生错误！查询失败！")
        else:
            return packinfo(infostatus=True, inforesult=crlist, infomsg="查询成功！")

    @staticmethod
    def addclassroom(params):
        """
        添加教室
        """
        classroom = params
        classroom_name = classroom["classroom_name"]
        classroom_position = classroom["classroom_position"]
        classroom_available = classroom["classroom_available"]
        cr = Classroom(classroom_name=classroom_name, classroom_position=classroom_position,
                       classroom_available=classroom_available)
        try:
            gdb.session.add(cr)
            gdb.session.commit()
        except Exception as e:
            return packinfo(infostatus=False, infomsg="数据库错误！教室添加失败！")
        else:
            return packinfo(infostatus=True, infomsg="教室添加成功！")

    @staticmethod
    def removeclassroom(classroomid):
        """
        删除教室
        """
        cr = gdb.session.query(Classroom).filter(Classroom.classroom_id==classroomid).first()
        if cr:
            foreigns = gdb.session.query(Class1).filter(
                Class1.classroom_id == classroomid).first()
            if foreigns:
                return packinfo(infostatus=False, infomsg="该教室信息正在被班级管理使用，为保证数据一致性，不可删除！")
            foreigns = gdb.session.query(Arrangement).filter(
                Arrangement.classroom_id == classroomid).first()
            if foreigns:
                return packinfo(infostatus=False, infomsg="该教室信息正在被排课管理使用，为保证数据一致性，不可删除！")
            try:
                gdb.session.delete(cr)
                gdb.session.commit()
            except Exception as e:
                return packinfo(infostatus=False, infomsg="数据库错误！教室删除失败！")
            else:
                return packinfo(infostatus=True, infomsg="教室删除成功！")
        else:
            return packinfo(infostatus=False, infomsg="教室编号不存在！教室删除失败！")

    @staticmethod
    def checkavailabletime(classroomid, week, section):
        """
        判断某一天某一节该教室是否可用
        """
        cr = gdb.session.query(Classroom).filter(Classroom.classroom_id==classroomid).first()
        if cr:
            if checkavailable(cr.classroom_available, week, section):
                return packinfo(infostatus=True, infomsg="教室可用！")
            else:
                return packinfo(infostatus=False, infomsg="教室不可用！")
        else:
            return packinfo(infostatus=False, infomsg="教室编号不存在！")

    @staticmethod
    def updateclassroom(classroomid, params):
        """
        更新教室
        """
        classroom = params
        classroom_name = classroom["classroom_name"]
        classroom_position = classroom["classroom_position"]
        classroom_available = classroom["classroom_available"]
        cr = gdb.session.query(Classroom).filter(Classroom.classroom_id==classroomid).first()
        if cr:
            try:
                cr.classroom_name = classroom_name
                cr.classroom_position = classroom_position
                cr.classroom_available = classroom_available
                gdb.session.commit()
            except Exception as e:
                return packinfo(infostatus=False, infomsg="数据库错误！教室更新失败！")
            else:
                return packinfo(infostatus=True, infomsg="教室更新成功！")
        else:
            return packinfo(infostatus=False, infomsg="教室编号不存在！教室更新失败！")