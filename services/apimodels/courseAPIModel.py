from appbase import global_api
from flask_restplus import fields

# course_classlist采用字符串拼接

coursemodel = global_api.model("Course", {
    "course_name": fields.String(required=True, description="课程名称"),
    "course_isgroup": fields.Boolean(required=True, description="是否合班"),
    "course_classlist": fields.String(description="合班清单")
})
