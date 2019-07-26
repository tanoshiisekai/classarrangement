from appbase import global_db as gdb


class Class1(gdb.Model):
    __tablename__ = 'class1'
    class_id = gdb.Column(gdb.Integer, primary_key=True)
    class_name = gdb.Column(gdb.String(100), nullable=False)
    teacher_id = gdb.Column(gdb.Integer, gdb.ForeignKey("teacher.teacher_id"))
    classroom_id = gdb.Column(gdb.Integer, gdb.ForeignKey("classroom.classroom_id"))
    
    def __init__(self, class_name, teacher_id, classroom_id):
        self.class_name = class_name
        self.teacher_id = teacher_id
        self.classroom_id = classroom_id
    
    def todict(self):
        return {
            "class_id": self.class_id,
            "class_name": self.class_name,
            "teacher_id": self.teacher_id,
            "classroom_id": self.classroom_id
        }
