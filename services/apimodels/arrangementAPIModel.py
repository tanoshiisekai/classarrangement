from appbase import global_api
from flask_restplus import fields


arrangementmodel = global_api.model("Arrangement", {
    "class_id": fields.Integer(required=True, description="班级编号"),
    "course_id": fields.Integer(required=True, description="课程编号"),
    "classroom_id": fields.Integer(required=True, description="教室编号"),
    "coursetime": fields.String(required=True, description="上课时间"),
    "ignoreclassroom": fields.Integer(required=True, description="是否忽略教室冲突"),
    "ignoreteacher": fields.Integer(required=True, description="是否忽略任课老师冲突"),
    "ignorecoursetime": fields.Integer(required=True, description="是否忽略时间冲突"),
})

