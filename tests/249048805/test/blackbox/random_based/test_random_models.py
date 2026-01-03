import random
import string
import pytest
from models.lecturer import Lecturer
from models.course import Course

# Black-box: Random-Based Testing

def rstr(n=8):
    return "".join(random.choice(string.ascii_letters) for _ in range(n))

def test_random_invalid_emails_fail():
    for _ in range(30):
        bad = rstr(10)  # no '@'
        with pytest.raises(ValueError):
            Lecturer(lecturer_id="L001", name="Dr", email=bad)

def test_random_course_levels_non_positive_fail():
    for _ in range(30):
        level = random.randint(-20, 0)
        with pytest.raises(ValueError):
            Course(course_id="C001", name="X", code="CO7095", level=level)
