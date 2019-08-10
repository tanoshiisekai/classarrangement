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
