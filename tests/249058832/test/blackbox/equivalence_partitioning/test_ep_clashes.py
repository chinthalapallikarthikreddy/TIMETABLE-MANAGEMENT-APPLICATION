# Black-box: EP for clash outcomes (no clash / lecturer clash / room clash / both)

from tests.test_utils.factories import make_entry

# UPDATE THIS import to match your project
# Example possibilities:
# from services.clash_service import ClashService
# from services.timetable_service import TimetableService
from services.clash_service import ClashService


def test_no_clash_partition():
    existing = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    new = make_entry("C002", "L002", "R102", "Monday", "09:30", "10:30")
    errors = ClashService.validate_no_clashes(existing, new)
    assert errors == []


def test_lecturer_clash_partition():
    existing = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    new = make_entry("C002", "L001", "R102", "Monday", "09:30", "10:30")
    errors = ClashService.validate_no_clashes(existing, new)
    assert any("Lecturer clash" in e for e in errors)


def test_room_clash_partition():
    existing = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    new = make_entry("C002", "L002", "R101", "Monday", "09:30", "10:30")
    errors = ClashService.validate_no_clashes(existing, new)
    assert any("Room clash" in e for e in errors)


def test_both_clash_partition():
    existing = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    new = make_entry("C002", "L001", "R101", "Monday", "09:30", "10:30")
    errors = ClashService.validate_no_clashes(existing, new)
    assert any("Lecturer clash" in e for e in errors)
    assert any("Room clash" in e for e in errors)
