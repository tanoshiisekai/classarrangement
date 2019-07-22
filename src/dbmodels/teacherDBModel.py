from appbase import global_db as gdb


class Teacher(gdb.Model):
    __tablename__ = 'teacher'
    teacher_id = gdb.Column(gdb.Integer, primary_key=True)
    teacher_name = gdb.Column(gdb.String(30), nullable=False)
    teacher_mobile = gdb.Column(gdb.String(30))
    teacher_request = gdb.Column(gdb.String(200))

    def __init__(self, teacher_id, teacher_name, teacher_mobile, teacher_request):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.teacher_mobile = teacher_mobile
        self.teacher_request = teacher_request

    def todict(self):
        return {
            "teacher_id": self.teacher_id,
            "teacher_name": self.teacher_name,
            "teacher_mobile": self.teacher_mobile,
            "teacher_request": self.teacher_request
        }
