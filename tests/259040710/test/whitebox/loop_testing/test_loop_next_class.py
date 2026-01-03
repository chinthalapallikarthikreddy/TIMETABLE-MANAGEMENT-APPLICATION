# White-box: Loop testing for scanning entries list

from tests.test_utils.factories import make_entry
from services.search_service import find_next_class


def test_loop_scans_all_entries_finds_last_match():
    entries = [
        make_entry("C001", "L001", "R101", "Monday", "08:00", "09:00"),
        make_entry("C002", "L002", "R102", "Monday", "09:00", "10:00"),
        make_entry("C003", "L003", "R103", "Monday", "10:00", "11:00"),
    ]
    nxt = find_next_class(entries, current_day="Monday", current_time="09:30")
    assert nxt is not None
