from appbase import global_db as gdb


class Course(gdb.Model):
    __tablename__ = 'course'
    course_id = gdb.Column(gdb.Integer, primary_key=True)
    course_name = gdb.Column(gdb.String(100), nullable=False)
    course_isgroup = gdb.Column(gdb.Boolean, nullable=False)
    
    def __init__(self, course_id, course_name, course_isgroup):
        self.course_id = course_id
        self.course_name = course_name
        self.course_isgroup = course_isgroup

    def todict(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "course_isgroup": self.course_isgroup
        }
