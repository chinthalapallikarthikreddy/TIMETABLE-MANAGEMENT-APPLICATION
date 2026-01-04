import pytest
from models.course import Course
from models.lecturer import Lecturer
from models.timeslot import Timeslot

# White-box: Branch Coverage (force each validation branch)

def test_course_missing_id_branch():
    with pytest.raises(ValueError):
        Course(course_id="", name="X", code="CO7095", level=7)

def test_course_missing_code_branch():
    with pytest.raises(ValueError):
        Course(course_id="C001", name="X", code="", level=7)

def test_course_level_invalid_branch():
    with pytest.raises(ValueError):
        Course(course_id="C001", name="X", code="CO7095", level=0)

def test_lecturer_bad_email_branch():
    with pytest.raises(ValueError):
        Lecturer(lecturer_id="L001", name="Dr", email="invalid")

def test_timeslot_invalid_range_branch():
    with pytest.raises(ValueError):
        Timeslot(day="Monday", start_time="10:00", end_time="09:00")
