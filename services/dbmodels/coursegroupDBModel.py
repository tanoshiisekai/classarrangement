from appbase import global_db as gdb


class CourseGroup(gdb.Model):
    __tablename__ = 'coursegroup'
    coursegroup_id = gdb.Column(gdb.Integer, primary_key=True)
    course_id = gdb.Column(gdb.Integer, gdb.ForeignKey("course.course_id"))
    class_id = gdb.Column(gdb.Integer, gdb.ForeignKey("class1.class_id"))
    
    def __init__(self, course_id, class_id):
        self.course_id = course_id
        self.class_id = class_id

    def todict(self):
        return {
            "coursegroup_id": self.coursegroup_id,
            "course_id": self.course_id,
            "class_id": self.class_id
        }
