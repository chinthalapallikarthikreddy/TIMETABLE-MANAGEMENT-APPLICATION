import pytest
from models.course import Course
from models.lecturer import Lecturer
from models.timeslot import Timeslot

# Black-box: Equivalence Partitioning (valid/invalid partitions)

def test_course_valid_partition():
    c = Course(course_id="C001", name="X", code="CO7095", level=7)
    assert c.course_id == "C001"

def test_course_invalid_partition_missing_id():
    with pytest.raises(ValueError):
        Course(course_id="", name="X", code="CO7095", level=7)

def test_lecturer_valid_partition():
    l = Lecturer(lecturer_id="L001", name="Dr A", email="a@b")
    assert l.lecturer_id == "L001"

def test_lecturer_invalid_partition_bad_email():
    with pytest.raises(ValueError):
        Lecturer(lecturer_id="L001", name="Dr A", email="ab.com")

def test_timeslot_valid_partition():
    t = Timeslot(day="Monday", start_time="09:00", end_time="10:00")
    assert t.day == "Monday"

def test_timeslot_invalid_partition_start_after_end():
    with pytest.raises(ValueError):
        Timeslot(day="Monday", start_time="10:00", end_time="09:00")
