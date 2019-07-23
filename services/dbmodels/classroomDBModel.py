from appbase import global_db as gdb


class Classroom(gdb.Model):
    __tablename__ = 'classroom'
    classroom_id = gdb.Column(gdb.Integer, primary_key=True)
    classroom_name = gdb.Column(gdb.String(50), nullable=False)
    classroom_position = gdb.Column(gdb.String(100), nullable=False)
    classroom_available = gdb.Column(gdb.String(200))

    def __init__(self, classroom_name, classroom_position, classroom_available):
        self.classroom_name = classroom_name
        self.classroom_position = classroom_position
        self.classroom_available = classroom_available

    def todict(self):
        return {
            "classroom_id": self.classroom_id,
            "classroom_name": self.classroom_name,
            "classroom_position": self.classroom_position,
            "classroom_available": self.classroom_available
        }
