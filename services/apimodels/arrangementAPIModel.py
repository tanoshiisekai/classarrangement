from appbase import global_api
from flask_restplus import fields


arrangementmodel = global_api.model("Arrangement", {
    "class_id": fields.Integer(required=True, description="班级编号"),
    "course_id": fields.Integer(required=True, description="课程编号"),
    "classroom_id": fields.Integer(required=True, description="教室编号"),
    "arrangement_week": fields.String(required=True, description="星期"),
    "arrangement_section": fields.String(required=True, description="节次")
})

