from appbase import global_api as api
from apimodels.arrangementAPIModel import arrangementmodel
from daos.arrangementDAO import ArrangementDAO
from flask_restplus import Resource

ns_arrangement = api.namespace("arrangement", description="排课管理")


@ns_arrangement.route("/")
class Arrangement(Resource):

    @ns_arrangement.expect(arrangementmodel)
    def post(self):
        """
        添加排课
        """
        return ArrangementDAO.addarrangement(api.payload)


@ns_arrangement.route("/teacher/<int:teacherid>")
class ArrangementTeacher(Resource):

    def get(self, teacherid):
        """
        返回教师课表
        """
        return ArrangementDAO.getteacherarrangement(teacherid)


@ns_arrangement.route("/remove/<int:classid>/<int:courseid>")
class RemoveArrangement(Resource):

    def get(self, classid, courseid):
        """
        移除排课
        """
        return ArrangementDAO.removearrangement(classid, courseid)


@ns_arrangement.route("/<int:class1id>/<string:week1>/<string:section1>/<int:class2id>/<string:week2>/<string:section2>/")
class Change(Resource):

    def get(self, class1id, week1, section1, class2id, week2, section2):
        """
        调课
        """
        return ArrangementDAO.changearrangement(class1id, week1, section1, class2id, week2, section2)
