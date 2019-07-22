from appbase import global_api as api
from apimodels.classAPIModel import classmodel
from daos.classDAO import ClassDAO
from flask_restplus import Resource

ns_class = api.namespace("class", description="班级管理")


@ns_class.route("/")
class Class1(Resource):

    def get(self):
        """
        返回所有班级，不查询包含的其他信息
        """
        return ClassDAO.getallclass()

    @ns_class.expect(classmodel)
    def post(self):
        """
        添加班级
        """
        return ClassDAO.addclass(api.payload)

    
@ns_class.route("/details/")
class ClassALLDetails(Resource):

    def get(self):
        """
        返回所有班级的详细信息，查询包含的其他信息
        """
        return ClassDAO.getallclassdetails()


@ns_class.route("/details/<int:classid>")
class ClassDetails(Resource):

    def get(self, classid):
        """
        根据班级编号返回详细信息，查询包含的其他信息
        """
        return ClassDAO.getclassdetailsbyid(classid)


@ns_class.route("/<int:classid>")
class ClassFind(Resource):

    def get(self, classid):
        """
        根据班级编号查询班级
        """
        return ClassDAO.getclassbyid(classid)


@ns_class.route("/remove/<int:classid>")
class ClassRemove(Resource):

    def get(self, classid):
        """
        根据班级编号删除班级
        """
        return ClassDAO.removeclass(classid)
