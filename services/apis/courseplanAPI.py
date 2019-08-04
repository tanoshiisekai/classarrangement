from appbase import global_api as api
from apimodels.courseplanAPIModel import courseplanmodel
from daos.courseplanDAO import CoursePlanDAO
from flask_restplus import Resource

ns_courseplan = api.namespace("courseplan", description="分课时管理")

@ns_courseplan.route("/")
class CoursePlan(Resource):

    def get(self):
        """
        返回所有分课时
        """
        return CoursePlanDAO.getallcourseplan()

    @ns_courseplan.expect(courseplanmodel)
    def post(self):
        """
        添加分课时
        """
        return CoursePlanDAO.addcourseplan(api.payload)
    

@ns_courseplan.route("/<int:courseplanid>")
class CoursePlanGet(Resource):

    def get(self, courseplanid):
        """
        根据分课时编号查询分课时
        """
        return CoursePlanDAO.getcourseplanbyid(courseplanid)


@ns_courseplan.route("/details/")
class CoursePlanDetails(Resource):

    def get(self):
        """
        返回所有分课时详情
        """
        return CoursePlanDAO.getallcourseplandetails()


@ns_courseplan.route("/details/<int:courseplanid>")
class CoursePlanDetails(Resource):

    def get(self, courseplanid):
        """
        根据编号返回分课时详情
        """
        return CoursePlanDAO.getallcourseplandetailsbyid(courseplanid)


@ns_courseplan.route("/remove/<int:courseplanid>")
class CoursePlanRemove(Resource):

    def get(self, courseplanid):
        """
        根据分课时编号删除分课时
        """
        return CoursePlanDAO.removecourseplan(courseplanid)

@ns_courseplan.route("/update/<int:courseplanid>")
class CoursePlanUpdate(Resource):

    @ns_courseplan.expect(courseplanmodel)
    def post(self, courseplanid):
        """
        根据分课时编号更新分课时
        """
        return CoursePlanDAO.updatecourseplan(courseplanid, api.payload)
