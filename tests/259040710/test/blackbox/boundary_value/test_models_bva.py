import pytest

from models.course import Course
from models.lecturer import Lecturer
from models.timeslot import Timeslot


# Black-box technique: Boundary Value Analysis (BVA)
# Focus: values around boundaries that trigger validation


def test_course_level_boundary_zero_fails():
    with pytest.raises(ValueError):
        Course(course_id="C001", name="Test", code="CO7095", level=0)


def test_course_level_boundary_one_passes():
    c = Course(course_id="C001", name="Test", code="CO7095", level=1)
    assert c.level == 1


def test_course_missing_course_id_fails():
    with pytest.raises(ValueError):
        Course(course_id="", name="Test", code="CO7095", level=7)


def test_course_missing_code_fails():
    with pytest.raises(ValueError):
        Course(course_id="C001", name="Test", code="", level=7)


def test_lecturer_email_missing_at_fails():
    with pytest.raises(ValueError):
        Lecturer(lecturer_id="L001", name="Dr A", email="invalid-email")


def test_lecturer_email_min_valid_passes():
    l = Lecturer(lecturer_id="L001", name="Dr A", email="a@b")
    assert l.email == "a@b"


def test_timeslot_equal_times_fails():
    with pytest.raises(ValueError):
        Timeslot(day="Monday", start_time="10:00", end_time="10:00")


def test_timeslot_one_minute_difference_passes():
    t = Timeslot(day="Monday", start_time="10:00", end_time="10:01")
    assert t.start_time == "10:00"
    assert t.end_time == "10:01"
