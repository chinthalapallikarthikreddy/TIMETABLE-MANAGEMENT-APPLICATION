from typing import List, Optional
from models.timetable_entry import TimetableEntry


def parse_time_to_minutes(t: str) -> int:
    h, m = t.split(":")
    return int(h) * 60 + int(m)


def normalize_day(day: str) -> str:
    return day.strip().lower()


def day_to_index(day: str) -> int:
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    return days.index(normalize_day(day))


def is_overlap(s1, e1, s2, e2) -> bool:
    return not (e1 <= s2 or s1 >= e2)


class SearchService:
    """
    Class-based search logic used by the application.
    """

    def next_class(
        self,
        entries: List[TimetableEntry],
        current_day: str,
        current_time: str,
        course_code=None,
        lecturer_id=None,
    ) -> Optional[TimetableEntry]:

        now_day_idx = day_to_index(current_day)
        now_time = parse_time_to_minutes(current_time)

        future = []

        for e in entries:
            e_day_idx = day_to_index(e.timeslot.day)
            e_start = parse_time_to_minutes(e.timeslot.start_time)

            if e_day_idx < now_day_idx:
                continue
            if e_day_idx == now_day_idx and e_start <= now_time:
                continue

            if course_code and e.course.code != course_code:
                continue
            if lecturer_id and e.lecturer.lecturer_id != lecturer_id:
                continue

            future.append((e_day_idx, e_start, e))

        if not future:
            return None

        future.sort(key=lambda x: (x[0], x[1]))
        return future[0][2]


# ================================
# FUNCTIONAL WRAPPER (CRITICAL)
# ================================

def find_next_class(entries, current_day, current_time, course_code=None, lecturer_id=None):
    """
    Wrapper required for Black-box, White-box, Loop, and Symbolic tests.
    """
    service = SearchService()
    return service.next_class(
        entries=entries,
        current_day=current_day,
        current_time=current_time,
        course_code=course_code,
        lecturer_id=lecturer_id,
    )
