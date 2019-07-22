from appbase import global_api
from flask_restplus import fields


classmodel = global_api.model("Class", {
    "class_id": fields.Integer(required=True, description="班级编号"),
    "class_name": fields.String(required=True, description="班级名称"),
    "teacher_id": fields.Integer(required=True, description="班主任编号"),
    "classroom_id": fields.Integer(required=True, description="默认教室编号")
})

