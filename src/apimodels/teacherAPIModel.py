from appbase import global_api
from flask_restplus import fields


teachermodel = global_api.model("Teacher", {
    "teacher_name": fields.String(required=True, description="教师姓名"),
    "teacher_mobile": fields.String(description="教师手机号"),
    "teacher_request": fields.String(description="可以上课的时间")
})

