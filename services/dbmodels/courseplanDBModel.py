from appbase import global_db as gdb


class CoursePlan(gdb.Model):
    __tablename__ = 'courseplan'
    courseplan_id = gdb.Column(gdb.Integer, primary_key=True)
    class_id = gdb.Column(gdb.Integer, gdb.ForeignKey("class1.class_id"))
    course_id = gdb.Column(gdb.Integer, gdb.ForeignKey("course.course_id"))
    teacher_id = gdb.Column(gdb.Integer, gdb.ForeignKey("teacher.teacher_id"))
    courseplan_count = gdb.Column(gdb.Integer, nullable=False)
    
    def __init__(self, class_id, course_id, teacher_id, courseplan_count):
        self.class_id = class_id
        self.course_id = course_id
        self.teacher_id = teacher_id
        self.courseplan_count = courseplan_count

    def todict(self):
        return {
            "courseplan_id": self.courseplan_id,
            "class_id": self.class_id,
            "course_id": self.course_id,
            "teacher_id": self.teacher_id,
            "courseplan_count": self.courseplan_count
        }
