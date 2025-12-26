from typing import List

WEEKDAY_ORDER: List[str] = [
    "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"
]


def normalize_day(day: str) -> str:
    if day is None:
        return ""
    return day.strip().lower()


def day_to_index(day: str) -> int:
    d = normalize_day(day)
    if d not in WEEKDAY_ORDER:
        raise ValueError(f"Invalid day '{day}'. Expected one of: {', '.join(WEEKDAY_ORDER)}")
    return WEEKDAY_ORDER.index(d)


def parse_time_to_minutes(time_str: str) -> int:
    """
    Expected format: 'HH:MM' (24-hour)
    Returns total minutes since 00:00.
    """
    if time_str is None:
        raise ValueError("Time cannot be None")

    s = time_str.strip()
    parts = s.split(":")
    if len(parts) != 2:
        raise ValueError("Time must be in HH:MM format")

    hh, mm = parts[0], parts[1]
    if not (hh.isdigit() and mm.isdigit()):
        raise ValueError("Time must contain digits only in HH:MM")

    h = int(hh)
    m = int(mm)

    if h < 0 or h > 23:
        raise ValueError("Hour must be between 00 and 23")
    if m < 0 or m > 59:
        raise ValueError("Minute must be between 00 and 59")

    return h * 60 + m


def is_overlap(start1: str, end1: str, start2: str, end2: str) -> bool:
    """
    Overlap check for time ranges on same day.
    """
    s1 = parse_time_to_minutes(start1)
    e1 = parse_time_to_minutes(end1)
    s2 = parse_time_to_minutes(start2)
    e2 = parse_time_to_minutes(end2)

    if s1 >= e1 or s2 >= e2:
        # invalid ranges should be caught earlier, but keep safe
        raise ValueError("Invalid time range: start must be before end")

    return not (e1 <= s2 or e2 <= s1)
