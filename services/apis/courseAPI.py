from appbase import global_api as api
from apimodels.courseAPIModel import coursemodel
from daos.courseDAO import CourseDAO
from flask_restplus import Resource

ns_course = api.namespace("course", description="课程管理")

@ns_course.route("/")
class Course(Resource):

    def get(self):
        """
        返回所有课程
        """
        return CourseDAO.getallcourse()

    @ns_course.expect(coursemodel)
    def post(self):
        """
        添加课程
        """
        return CourseDAO.addcourse(api.payload)

    
@ns_course.route("/details/")
class CourseALLDetails(Resource):

    def get(self):
        """
        返回所有课程的详细信息，查询包含的其他信息
        """
        return CourseDAO.getallcoursedetails()


@ns_course.route("/details/<int:courseid>")
class CourseDetails(Resource):

    def get(self, courseid):
        """
        根据课程编号返回详细信息，查询包含的其他信息
        """
        return CourseDAO.getcoursedetailsbyid(courseid)


@ns_course.route("/<int:courseid>")
class CourseFind(Resource):

    def get(self, courseid):
        """
        根据课程编号查询课程
        """
        return CourseDAO.getcoursebyid(courseid)


@ns_course.route("/remove/<int:courseid>")
class CourseRemove(Resource):

    def get(self, courseid):
        """
        根据课程编号删除课程
        """
        return CourseDAO.removecourse(courseid)


@ns_course.route("/update/<int:courseid>")
class CourseUpdate(Resource):

    @ns_course.expect(coursemodel)
    def post(self, courseid):
        """
        根据课程编号更新课程
        """
        return CourseDAO.updatecourse(courseid, api.payload)
