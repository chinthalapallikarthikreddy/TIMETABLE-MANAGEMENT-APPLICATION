from typing import Any, Dict, Optional
from utils.time_utils import day_to_index, parse_time_to_minutes


def require_non_empty(value: str, field_name: str) -> str:
    if value is None or str(value).strip() == "":
        raise ValueError(f"{field_name} is required")
    return str(value).strip()


def validate_day(day: str) -> str:
    d = require_non_empty(day, "day")
    # day_to_index raises if invalid
    day_to_index(d)
    return d.strip()


def validate_time(time_str: str, field_name: str) -> str:
    t = require_non_empty(time_str, field_name)
    parse_time_to_minutes(t)  # raises if invalid
    return t


def validate_time_range(start_time: str, end_time: str) -> None:
    s = parse_time_to_minutes(start_time)
    e = parse_time_to_minutes(end_time)
    if s >= e:
        raise ValueError("Start time must be before end time")


def require_exists(store: Dict[str, Any], key: str, field_name: str) -> Any:
    if key not in store:
        raise ValueError(f"{field_name} '{key}' does not exist")
    return store[key]


def optional_str(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    v = value.strip()
    return v if v != "" else None
