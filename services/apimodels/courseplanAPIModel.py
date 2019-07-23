from appbase import global_api
from flask_restplus import fields


courseplanmodel = global_api.model("CoursePlan", {
    "class_id": fields.Integer(required=True, description="班级编号"),
    "course_id": fields.Integer(required=True, description="课程编号"),
    "teacher_id": fields.Integer(required=True, description="教师编号"),
    "courseplan_count": fields.Integer(required=True, description="课时数")
})

