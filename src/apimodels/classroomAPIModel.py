from appbase import global_api
from flask_restplus import fields


classroommodel = global_api.model("Classroom", {
    "classroom_name": fields.String(required=True, description="教室名称"),
    "classroom_position": fields.String(required=True, description="教室位置"),
    "classroom_available": fields.String(description="教室可用时间")
})

