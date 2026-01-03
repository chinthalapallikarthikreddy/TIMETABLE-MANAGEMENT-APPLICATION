import importlib
from tests.test_utils.factories import make_entry


def _get_next_class_fn():
    ss = importlib.import_module("services.search_service")
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


def test_loop_scans_all_entries_finds_last_match():
    fn = _get_next_class_fn()
    entries = [
        make_entry("C001", "L001", "R101", "Monday", "08:00", "09:00"),
        make_entry("C002", "L002", "R102", "Monday", "09:00", "10:00"),
        make_entry("C003", "L003", "R103", "Monday", "10:00", "11:00"),
    ]
    nxt = fn(entries, current_day="Monday", current_time="09:30")
    assert nxt is not None
