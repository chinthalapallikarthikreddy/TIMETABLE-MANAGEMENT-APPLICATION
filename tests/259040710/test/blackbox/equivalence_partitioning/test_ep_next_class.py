# Black-box: EP for next class (no entries / one entry / multiple entries)

from tests.test_utils.factories import make_entry

# UPDATE this import to your real function
# Example:
# from services.search_service import find_next_class
from services.search_service import find_next_class


def test_no_entries_partition_returns_none():
    assert find_next_class([], current_day="Monday", current_time="08:00") is None


def test_one_entry_partition_returns_that_entry():
    entries = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    nxt = find_next_class(entries, current_day="Monday", current_time="08:00")
    assert nxt is not None


def test_multiple_entries_partition_returns_earliest_after_time():
    entries = [
        make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00"),
        make_entry("C002", "L002", "R102", "Monday", "11:00", "12:00"),
    ]
    nxt = find_next_class(entries, current_day="Monday", current_time="08:30")
    assert nxt is not None
