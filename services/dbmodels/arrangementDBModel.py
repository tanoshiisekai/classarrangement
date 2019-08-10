from appbase import global_db as gdb


class Arrangement(gdb.Model):
    __tablename__ = 'arrangement'
    arrangement_id = gdb.Column(gdb.Integer, primary_key=True)
    class_id = gdb.Column(gdb.Integer, gdb.ForeignKey("class1.class_id"))
    course_id = gdb.Column(gdb.Integer, gdb.ForeignKey("course.course_id"))
    classroom_id = gdb.Column(gdb.Integer, gdb.ForeignKey("classroom.classroom_id"))
    teacher_id = gdb.Column(gdb.Integer, gdb.ForeignKey("teacher.teacher_id"))
    arrangement_week = gdb.Column(gdb.String(5), nullable=False)
    arrangement_section = gdb.Column(gdb.String(5), nullable=False)
    
    def __init__(self, class_id, course_id, classroom_id, teacher_id, arrangement_week, arrangement_section):
        self.class_id = class_id
        self.course_id = course_id
        self.classroom_id = classroom_id
        self.teacher_id = teacher_id
        self.arrangement_week = arrangement_week
        self.arrangement_section = arrangement_section

    def todict(self):
        return {
            "arrangement_id": self.arrangement_id,
            "class_id": self.class_id,
            "course_id": self.course_id,
            "classroom_id": self.classroom_id,
            "teacher_id": self.teacher_id,
            "arrangement_week": self.arrangement_week,
            "arrangement_section": self.arrangement_section
        }
