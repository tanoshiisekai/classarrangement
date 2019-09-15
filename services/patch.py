from dbmodels.arrangementDBModel import Arrangement
from dbmodels.classDBModel import Class1
from dbmodels.courseDBModel import Course
from dbmodels.classroomDBModel import Classroom
from dbmodels.courseplanDBModel import CoursePlan
from dbmodels.coursegroupDBModel import CourseGroup
from appbase import global_db as gdb
from sqlalchemy import and_


def updateteacherarrangement():
    """
    临时修复由于班级更换教师导致的课时统计错误
    """
    datas = gdb.session.query(Arrangement).all()
    for dt in datas:
        temp = gdb.session.query(CoursePlan).filter(and_(
            CoursePlan.class_id == dt.class_id,
            CoursePlan.course_id == dt.course_id)).first()
        dt.teacher_id = temp.teacher_id
    gdb.session.commit()


# updateteacherarrangement()
