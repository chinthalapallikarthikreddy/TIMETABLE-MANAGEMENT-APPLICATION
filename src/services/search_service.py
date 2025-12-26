from typing import List, Optional
from utils.time_utils import normalize_day, day_to_index, parse_time_to_minutes, is_overlap


class SearchService:
    @staticmethod
    def next_class(
        entries,
        current_day: str,
        current_time: str,
        course_code: Optional[str] = None,
        lecturer_id: Optional[str] = None
    ):
        """
        Finds the next upcoming class based on weekday order and time.
        Assumes schedule repeats weekly.

        Filters:
        - course_code (optional)
        - lecturer_id (optional)
        """
        cur_day_idx = day_to_index(current_day)
        cur_minutes = parse_time_to_minutes(current_time)

        candidates = []

        for e in entries:
            if course_code is not None and e.course.code != course_code:
                continue
            if lecturer_id is not None and e.lecturer.lecturer_id != lecturer_id:
                continue

            e_day_idx = day_to_index(e.timeslot.day)
            e_start = parse_time_to_minutes(e.timeslot.start_time)

            # compute "distance" in minutes from current moment within a weekly cycle
            day_diff = (e_day_idx - cur_day_idx) % 7
            delta_minutes = day_diff * 24 * 60 + (e_start - cur_minutes)

            # if same day and already started, push it to next week
            if day_diff == 0 and e_start <= cur_minutes:
                delta_minutes += 7 * 24 * 60

            candidates.append((delta_minutes, e))

        if not candidates:
            return None

        candidates.sort(key=lambda x: x[0])
        return candidates[0][1]

    @staticmethod
    def find_free_rooms(
        entries,
        all_rooms: List[str],
        day: str,
        start_time: str,
        end_time: str
    ) -> List[str]:
        """
        Returns rooms that have no overlapping booking in the given time window on the given day.
        """
        d = normalize_day(day)
        requested_start = start_time
        requested_end = end_time

        free_rooms = []

        for room in all_rooms:
            occupied = False
            for e in entries:
                if e.room != room:
                    continue
                if normalize_day(e.timeslot.day) != d:
                    continue

                if is_overlap(e.timeslot.start_time, e.timeslot.end_time, requested_start, requested_end):
                    occupied = True
                    break

            if not occupied:
                free_rooms.append(room)

        return free_rooms
