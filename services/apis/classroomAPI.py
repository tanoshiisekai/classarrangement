from appbase import global_api as api
from apimodels.classroomAPIModel import classroommodel
from daos.classroomDAO import ClassroomDAO
from flask_restplus import Resource

ns_classroom = api.namespace("classroom", description="教室管理")

@ns_classroom.route("/")
class Classroom(Resource):

    def get(self):
        """
        返回所有教室
        """
        return ClassroomDAO.getallclassroom()

    @ns_classroom.expect(classroommodel)
    def post(self):
        """
        添加教室
        """
        return ClassroomDAO.addclassroom(api.payload)


@ns_classroom.route("/<int:classroomid>")
class ClassroomFind(Resource):
    
    def get(self, classroomid):
        """
        根据教室编号查询教室
        """
        return ClassroomDAO.getclassroombyid(classroomid)


@ns_classroom.route("/remove/<int:classroomid>")
class ClassroomRemove(Resource):

    def get(self, classroomid):
        """
        根据教室编号删除教室
        """
        return ClassroomDAO.removeclassroom(classroomid)


@ns_classroom.route("/check/<int:classroomid>/<string:week>/<string:section>")
class ClassroomCheck(Resource):

    def get(self, classroomid, week, section):
        """
        查询教室是否可用
        """
        return ClassroomDAO.checkavailabletime(classroomid, week, section)


@ns_classroom.route("/update/<int:classroomid>")
class ClassroomUpdate(Resource):

    @ns_classroom.expect(classroommodel)
    def post(self, classroomid):
        """
        根据教室编号更新教室
        """
        return ClassroomDAO.updateclassroom(classroomid, api.payload)
