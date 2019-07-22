from dbmodels.classroomDBModel import Classroom
from appbase import global_db as gdb
from flask import jsonify
from tools.info import Info


class ClassroomDAO:

    @staticmethod
    def addclassroom(params):
        classroom = params
        classroom_name = classroom["classroom_name"]
        classroom_position = classroom["classroom_position"]
        classroom_available = classroom["classroom_available"]
        cr = Classroom(classroom_name=classroom_name, classroom_position=classroom_position,
                       classroom_available=classroom_available)
        gdb.session.add(cr)
        gdb.session.commit()
        return jsonify(Info(infostatus=True, infomsg="教室添加成功!").tojson())
