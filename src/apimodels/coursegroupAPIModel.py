from appbase import global_api
from flask_restplus import fields


coursegroupmodel = global_api.model("CourseGroup", {
    "coursegroup_id": fields.Integer(required=True, description="合班课程编号"),
    "course_id": fields.Integer(required=True, description="课程编号"),
    "class_id": fields.Integer(required=True, description="班级编号")
})

