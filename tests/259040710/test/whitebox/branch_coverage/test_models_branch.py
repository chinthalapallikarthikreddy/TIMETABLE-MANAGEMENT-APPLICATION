import pytest

from models.course import Course
from models.lecturer import Lecturer
from models.timeslot import Timeslot


# White-box technique: Branch Coverage
# Goal: force each IF branch outcome at least once.


def test_course_validate_branch_missing_id_or_code():
    # Branch: (not course_id or not code) -> raises
    with pytest.raises(ValueError):
        Course(course_id="", name="Test", code="CO7095", level=7)

    with pytest.raises(ValueError):
        Course(course_id="C001", name="Test", code="", level=7)


def test_course_validate_branch_level_non_positive():
    # Branch: level <= 0 -> raises
    with pytest.raises(ValueError):
        Course(course_id="C001", name="Test", code="CO7095", level=0)


def test_course_validate_all_good_path():
    # No exception path
    c = Course(course_id="C001", name="Test", code="CO7095", level=7)
    assert c.code == "CO7095"


def test_lecturer_validate_branch_invalid_email():
    # Branch: "@" not in email -> raises
    with pytest.raises(ValueError):
        Lecturer(lecturer_id="L001", name="Dr A", email="invalid")


def test_lecturer_validate_valid_email_path():
    l = Lecturer(lecturer_id="L001", name="Dr A", email="a@b")
    assert "@" in l.email


def test_timeslot_validate_branch_invalid_range():
    # Branch: start_time >= end_time -> raises
    with pytest.raises(ValueError):
        Timeslot(day="Monday", start_time="10:00", end_time="09:00")


def test_timeslot_validate_valid_range_path():
    t = Timeslot(day="Monday", start_time="09:00", end_time="10:00")
    assert t.start_time == "09:00"
