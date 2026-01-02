from models.course import Course
from models.lecturer import Lecturer
from models.timeslot import Timeslot
from models.timetable_entry import TimetableEntry

# Update this import to your real function
from services.clash_service import ClashService


def make_entry(course_id, lecturer_id, room, day, start, end):
    c = Course(course_id=course_id, name="X", code="CO7095", level=7)
    l = Lecturer(lecturer_id=lecturer_id, name="Dr", email="a@b")
    return TimetableEntry(course=c, lecturer=l, room=room, timeslot=Timeslot(day, start, end))


def test_P1_no_overlap_no_errors():
    existing = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    new = make_entry("C002", "L001", "R101", "Monday", "10:00", "11:00")  # no overlap
    errors = ClashService.validate_no_clashes(existing, new)
    assert errors == []


def test_P2_overlap_but_different_lecturer_and_room_no_errors():
    existing = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    new = make_entry("C002", "L002", "R102", "Monday", "09:30", "10:30")  # overlap but no same lecturer/room
    errors = ClashService.validate_no_clashes(existing, new)
    assert errors == []


def test_P3_overlap_same_lecturer_only():
    existing = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    new = make_entry("C002", "L001", "R102", "Monday", "09:30", "10:30")  # lecturer clash only
    errors = ClashService.validate_no_clashes(existing, new)
    assert any("Lecturer clash" in e for e in errors)
    assert all("Room clash" not in e for e in errors)


def test_P4_overlap_same_room_only():
    existing = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    new = make_entry("C002", "L002", "R101", "Monday", "09:30", "10:30")  # room clash only
    errors = ClashService.validate_no_clashes(existing, new)
    assert any("Room clash" in e for e in errors)
    assert all("Lecturer clash" not in e for e in errors)


def test_P5_overlap_same_lecturer_and_room():
    existing = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    new = make_entry("C002", "L001", "R101", "Monday", "09:30", "10:30")  # both
    errors = ClashService.validate_no_clashes(existing, new)
    assert any("Lecturer clash" in e for e in errors)
    assert any("Room clash" in e for e in errors)
