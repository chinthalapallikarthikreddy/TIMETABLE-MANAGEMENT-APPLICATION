import importlib
from tests.test_utils.factories import make_entry


def _get_next_class_fn():
    ss = importlib.import_module("services.search_service")

    # Try common function names
    for name in [
        "find_next_class",
        "get_next_class",
        "next_class",
        "get_next_timetable_entry",
        "find_next_timetable_entry",
    ]:
        fn = getattr(ss, name, None)
        if callable(fn):
            return fn

    raise RuntimeError(
        "No next-class function found in services.search_service. "
        "Open src/services/search_service.py and add the correct function name to the list."
    )


def test_no_entries_partition_returns_none():
    fn = _get_next_class_fn()
    assert fn([], current_day="Monday", current_time="08:00") is None


def test_one_entry_partition_returns_that_entry():
    fn = _get_next_class_fn()
    entries = [make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00")]
    nxt = fn(entries, current_day="Monday", current_time="08:00")
    assert nxt is not None


def test_multiple_entries_partition_returns_earliest_after_time():
    fn = _get_next_class_fn()
    entries = [
        make_entry("C001", "L001", "R101", "Monday", "09:00", "10:00"),
        make_entry("C002", "L002", "R102", "Monday", "11:00", "12:00"),
    ]
    nxt = fn(entries, current_day="Monday", current_time="08:30")
    assert nxt is not None
