import pytest
from models.course import Course
from models.timeslot import Timeslot

# Black-box: Boundary Value Analysis (BVA)

def test_course_level_boundary_zero_fails():
    with pytest.raises(ValueError):
        Course(course_id="C001", name="X", code="CO7095", level=0)

def test_course_level_boundary_one_passes():
    c = Course(course_id="C001", name="X", code="CO7095", level=1)
    assert c.level == 1

def test_timeslot_equal_times_fails():
    with pytest.raises(ValueError):
        Timeslot(day="Monday", start_time="10:00", end_time="10:00")

def test_timeslot_one_minute_gap_passes():
    t = Timeslot(day="Monday", start_time="10:00", end_time="10:01")
    assert t.start_time == "10:00"
