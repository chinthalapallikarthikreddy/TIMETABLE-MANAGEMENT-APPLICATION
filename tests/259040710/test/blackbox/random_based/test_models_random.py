import random
import string
import pytest

from models.course import Course
from models.lecturer import Lecturer
from models.timeslot import Timeslot


# Black-box technique: Random-Based Testing
# Focus: randomly generated inputs to discover unexpected failures


def random_string(n=8):
    return "".join(random.choice(string.ascii_letters) for _ in range(n))


def test_random_invalid_emails_fail():
    # generate emails without '@' (invalid partition)
    for _ in range(30):
        bad_email = random_string(10)  # no '@'
        with pytest.raises(ValueError):
            Lecturer(lecturer_id="L001", name="Dr A", email=bad_email)


def test_random_course_levels_non_positive_fail():
    # random values in invalid partition: <= 0
    for _ in range(30):
        level = random.randint(-50, 0)
        with pytest.raises(ValueError):
            Course(course_id="C001", name="Test", code="CO7095", level=level)


def test_random_timeslot_valid_passes():
    # generate random valid timeslots (simple safe set)
    valid_times = [("09:00", "10:00"), ("10:00", "11:00"), ("13:00", "14:00")]
    for _ in range(20):
        start, end = random.choice(valid_times)
        t = Timeslot(day="Monday", start_time=start, end_time=end)
        assert t.start_time < t.end_time
