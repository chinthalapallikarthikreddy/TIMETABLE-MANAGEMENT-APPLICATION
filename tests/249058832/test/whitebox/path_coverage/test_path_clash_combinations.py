from tests.test_utils.factories import make_entry
from services.clash_service import ClashService

# White-box: Path coverage over (Overlap?) then (Lecturer match?) and (Room match?)

def test_path_P1_no_overlap():
    existing = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    new = make_entry("C002", "L001", "R101", "Monday", "10:00", "11:00")
    assert ClashService.validate_no_clashes(existing, new) == []

def test_path_P2_overlap_no_match():
    existing = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    new = make_entry("C002", "L002", "R102", "Monday", "09:30", "10:30")
    assert ClashService.validate_no_clashes(existing, new) == []

def test_path_P3_overlap_lecturer_only():
    existing = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    new = make_entry("C002", "L001", "R102", "Monday", "09:30", "10:30")
    errors = ClashService.validate_no_clashes(existing, new)
    assert any("Lecturer clash" in e for e in errors)

def test_path_P4_overlap_room_only():
    existing = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    new = make_entry("C002", "L002", "R101", "Monday", "09:30", "10:30")
    errors = ClashService.validate_no_clashes(existing, new)
    assert any("Room clash" in e for e in errors)

def test_path_P5_overlap_both():
    existing = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    new = make_entry("C002", "L001", "R101", "Monday", "09:30", "10:30")
    errors = ClashService.validate_no_clashes(existing, new)
    assert any("Lecturer clash" in e for e in errors)
    assert any("Room clash" in e for e in errors)
