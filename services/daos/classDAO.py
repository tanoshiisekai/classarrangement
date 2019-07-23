from dbmodels.classDBModel import Class1
from dbmodels.teacherDBModel import Teacher
from dbmodels.classroomDBModel import Classroom
from appbase import global_db as gdb
from tools.packtools import packinfo, packjoinquery
from sqlalchemy import and_


class ClassDAO:

    @staticmethod
    def getallclassdetails():
        """
        返回所有班级的详细信息
        """
        try:
            clalist = gdb.session.query(
                Class1, Teacher, Classroom).filter(
                    Class1.teacher_id == Teacher.teacher_id).filter(
                    Class1.classroom_id == Classroom.classroom_id).all()
            clalist = [packjoinquery(x) for x in clalist]
        except Exception as e:
            return packinfo(infostatus=False, infomsg="数据库无数据或发生错误！查询失败！")
        else:
            return packinfo(infostatus=True, inforesult=clalist, infomsg="查询成功！")

    @staticmethod
    def getclassdetailsbyid(classid):
        """
        根据班级编号查询班级详细信息
        """
        try:
            cla = gdb.session.query(
                Class1, Teacher, Classroom).filter(
                    Class1.class_id == classid).filter(
                    Class1.teacher_id == Teacher.teacher_id).filter(
                    Class1.classroom_id == Classroom.classroom_id).first()
            cla = packjoinquery(cla)
        except Exception as e:
            return packinfo(infostatus=False, infomsg="数据库无数据或发生错误！查询失败！")
        else:
            return packinfo(infostatus=True, inforesult=cla, infomsg="查询成功！")

    @staticmethod
    def getclassbyid(classid):
        """
        根据班级编号查询班级
        """
        try:
            cla = gdb.session.query(Class1).filter(
                Class1.class_id == classid).first()
            cla = cla.todict()
        except Exception as e:
            return packinfo(infostatus=False, infomsg="数据库无数据或发生错误！查询失败！")
        else:
            return packinfo(infostatus=True, inforesult=cla, infomsg="查询成功！")

    @staticmethod
    def getallclass():
        """
        返回所有班级
        """
        try:
            clalist = gdb.session.query(Class1).all()
            clalist = [x.todict() for x in clalist]
        except Exception as e:
            return packinfo(infostatus=False, infomsg="数据库无数据或发生错误！查询失败！")
        else:
            return packinfo(infostatus=True, inforesult=clalist, infomsg="查询成功！")

    @staticmethod
    def addclass(params):
        """
        添加班级
        """
        class1 = params
        class_name = class1["class_name"]
        teacher_id = class1["teacher_id"]
        classroom_id = class1["classroom_id"]
        cla = Class1(class_name=class_name, teacher_id=teacher_id,
                     classroom_id=classroom_id)
        try:
            gdb.session.add(cla)
            gdb.session.commit()
        except Exception as e:
            return packinfo(infostatus=False, infomsg="数据库错误！班级添加失败！")
        else:
            return packinfo(infostatus=True, infomsg="班级添加成功！")

    @staticmethod
    def removeclass(classid):
        """
        删除班级
        """
        cla = gdb.session.query(Class1).filter(
            Class1.class_id == classid).first()
        if cla:
            try:
                gdb.session.delete(cla)
                gdb.session.commit()
            except Exception as e:
                return packinfo(infostatus=False, infomsg="数据库错误！班级删除失败！")
            else:
                return packinfo(infostatus=True, infomsg="班级删除成功！")
        else:
            return packinfo(infostatus=False, infomsg="班级编号不存在！班级删除失败！")
