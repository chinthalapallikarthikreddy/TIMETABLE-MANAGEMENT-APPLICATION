from models.timeslot import Timeslot


# White-box technique: Path Coverage
# Target function: Timeslot.overlaps(other)
# Paths:
# P1: different day -> False
# P2: same day + non-overlapping -> False
# P3: same day + overlapping -> True


def test_overlaps_path_different_day_false():
    a = Timeslot(day="Monday", start_time="09:00", end_time="10:00")
    b = Timeslot(day="Tuesday", start_time="09:30", end_time="10:30")
    assert a.overlaps(b) is False


def test_overlaps_path_same_day_no_overlap_false_end_equals_start():
    a = Timeslot(day="Monday", start_time="09:00", end_time="10:00")
    b = Timeslot(day="Monday", start_time="10:00", end_time="11:00")
    assert a.overlaps(b) is False


def test_overlaps_path_same_day_overlap_true():
    a = Timeslot(day="Monday", start_time="09:00", end_time="10:00")
    b = Timeslot(day="Monday", start_time="09:30", end_time="10:30")
    assert a.overlaps(b) is True
