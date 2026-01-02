from models.course import Course
from models.lecturer import Lecturer
from models.timeslot import Timeslot
from models.timetable_entry import TimetableEntry


def make_course(course_id="C001", name="Test Course", code="CO7095", level=7):
    return Course(course_id=course_id, name=name, code=code, level=level)


def make_lecturer(lecturer_id="L001", name="Dr Test", email="test@uni.ac.uk"):
    return Lecturer(lecturer_id=lecturer_id, name=name, email=email)


def make_timeslot(day="Monday", start="09:00", end="10:00"):
    return Timeslot(day=day, start_time=start, end_time=end)


def make_entry(
    course_id="C001",
    lecturer_id="L001",
    room="R101",
    day="Monday",
    start="09:00",
    end="10:00"
):
    c = make_course(course_id=course_id)
    l = make_lecturer(lecturer_id=lecturer_id)
    t = make_timeslot(day=day, start=start, end=end)
    return TimetableEntry(course=c, lecturer=l, room=room, timeslot=t)
