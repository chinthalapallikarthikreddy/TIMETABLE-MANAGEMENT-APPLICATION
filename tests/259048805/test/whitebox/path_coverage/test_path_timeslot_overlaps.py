from models.timeslot import Timeslot

# White-box: Path Coverage for Timeslot.overlaps

def test_path_P1_different_day_false():
    a = Timeslot("Monday", "09:00", "10:00")
    b = Timeslot("Tuesday", "09:30", "10:30")
    assert a.overlaps(b) is False

def test_path_P2_same_day_no_overlap_false():
    a = Timeslot("Monday", "09:00", "10:00")
    b = Timeslot("Monday", "10:00", "11:00")
    assert a.overlaps(b) is False

def test_path_P3_same_day_overlap_true():
    a = Timeslot("Monday", "09:00", "10:00")
    b = Timeslot("Monday", "09:30", "10:30")
    assert a.overlaps(b) is True
