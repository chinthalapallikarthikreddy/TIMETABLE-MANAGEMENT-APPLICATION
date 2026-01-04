from __future__ import annotations

from typing import List, Optional

from models.timetable_entry import TimetableEntry


def parse_time_to_minutes(t: str) -> int:
    t = t.strip()
    h, m = t.split(":")
    return int(h) * 60 + int(m)


def normalize_day(day: str) -> str:
    return day.strip().lower()


def day_to_index(day: str) -> int:
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    return days.index(normalize_day(day))


def times_overlap(start_a: str, end_a: str, start_b: str, end_b: str) -> bool:
    a1 = parse_time_to_minutes(start_a)
    a2 = parse_time_to_minutes(end_a)
    b1 = parse_time_to_minutes(start_b)
    b2 = parse_time_to_minutes(end_b)
    return a1 < b2 and b1 < a2


class SearchService:
    """
    Search utilities:
    - next_class: finds the next scheduled class from a given day+time
      (scans the rest of the week as well, not just the same day)
    - find_free_rooms: returns rooms not booked in a given interval
    """

    @staticmethod
    def next_class(entries: List[TimetableEntry], current_day: str, current_time: str) -> Optional[TimetableEntry]:
        if not entries:
            return None

        cur_day_idx = day_to_index(current_day)
        cur_time_min = parse_time_to_minutes(current_time)

        best = None
        best_key = None  # (delta_days, start_minutes)

        for e in entries:
            e_day_idx = day_to_index(e.timeslot.day)
            delta = (e_day_idx - cur_day_idx) % 7

            e_start_min = parse_time_to_minutes(e.timeslot.start_time)

            # If same day, it must be strictly after the current time
            if delta == 0 and e_start_min <= cur_time_min:
                continue

            key = (delta, e_start_min)
            if best_key is None or key < best_key:
                best_key = key
                best = e

        return best

    @staticmethod
    def find_free_rooms(entries: List[TimetableEntry], rooms: List[str], day: str, start: str, end: str) -> List[str]:
        if not rooms:
            return []

        d = normalize_day(day)
        free = []

        for r in rooms:
            booked = False
            for e in entries:
                if normalize_day(e.timeslot.day) != d:
                    continue
                if e.room != r:
                    continue
                if times_overlap(start, end, e.timeslot.start_time, e.timeslot.end_time):
                    booked = True
                    break

            if not booked:
                free.append(r)

        free.sort()
        return free


# ================================
# FUNCTIONAL WRAPPERS (for tests)
# ================================

def find_next_class(entries: List[TimetableEntry], current_day: str, current_time: str) -> Optional[TimetableEntry]:
    return SearchService.next_class(entries, current_day, current_time)


def find_free_rooms(entries: List[TimetableEntry], rooms: List[str], day: str, start: str, end: str) -> List[str]:
    return SearchService.find_free_rooms(entries, rooms, day, start, end)
