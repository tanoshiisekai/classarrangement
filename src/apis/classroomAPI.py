from appbase import global_api as api
from apimodels.classroomAPIModel import classroommodel
from daos.classroomDAO import ClassroomDAO
from flask_restplus import Resource

ns_classroom = api.namespace("classroom", description="教室管理")

@ns_classroom.route("/")
class Classroom(Resource):

    @ns_classroom.expect(classroommodel)
    def post(self):
        return ClassroomDAO.addclassroom(api.payload)
