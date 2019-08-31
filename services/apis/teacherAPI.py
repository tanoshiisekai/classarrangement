from appbase import global_api as api
from apimodels.teacherAPIModel import teachermodel
from daos.teacherDAO import TeacherDAO
from flask_restplus import Resource

ns_teacher = api.namespace("teacher", description="教师管理")


@ns_teacher.route("/")
class Teacher(Resource):

    def get(self):
        """
        返回所有教师
        """
        return TeacherDAO.getallteacher()

    @ns_teacher.expect(teachermodel)
    def post(self):
        """
        添加教师
        """
        return TeacherDAO.addteacher(api.payload)


@ns_teacher.route("/<int:teacherid>")
class TeacherFind(Resource):

    def get(self, teacherid):
        """
        根据教师编号查询教师
        """
        return TeacherDAO.getteacherbyid(teacherid)


@ns_teacher.route("/<string:teachername>")
class TeacherFindName(Resource):

    def get(self, teachername):
        """
        根据教师姓名查询教师
        """
        return TeacherDAO.getteacherbyname(teachername)


@ns_teacher.route("/remove/<int:teacherid>")
class TeacherRemove(Resource):

    def get(self, teacherid):
        """
        根据教师编号删除教师
        """
        return TeacherDAO.removeteacher(teacherid)


@ns_teacher.route("/check/<int:teacherid>/<string:week>/<string:section>")
class TeacherCheck(Resource):

    def get(self, teacherid, week, section):
        """
        查询教师能否上课
        """
        return TeacherDAO.checkavailabletime(teacherid, week, section)


@ns_teacher.route("/update/<int:teacherid>")
class TeacherUpdate(Resource):

    @ns_teacher.expect(teachermodel)
    def post(self, teacherid):
        """
        根据教师编号更新教师
        """
        return TeacherDAO.updateteacher(teacherid, api.payload)
