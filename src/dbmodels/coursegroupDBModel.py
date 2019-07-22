from appbase import global_db as gdb


class CourseGroup(gdb.Model):
    __tablename__ = 'coursegroup'
    coursegroup_id = gdb.Column(gdb.Integer, primary_key=True)
    course_id = gdb.Column(gdb.Integer, nullable=False)
    class_id = gdb.Column(gdb.Integer, nullable=False)
    
    def __init__(self, coursegroup_id, course_id, class_id):
        self.coursegroup_id = coursegroup_id
        self.course_id = course_id
        self.class_id = class_id

    def todict(self):
        return {
            "coursegroup_id": self.coursegroup_id,
            "course_id": self.course_id,
            "class_id": self.class_id
        }
