from typing import List
from utils.time_utils import normalize_day, is_overlap


class ClashService:
    @staticmethod
    def lecturer_clash(existing_entries, new_entry) -> bool:
        new_day = normalize_day(new_entry.timeslot.day)

        for e in existing_entries:
            if e.lecturer.lecturer_id != new_entry.lecturer.lecturer_id:
                continue

            if normalize_day(e.timeslot.day) != new_day:
                continue

            if is_overlap(e.timeslot.start_time, e.timeslot.end_time,
                          new_entry.timeslot.start_time, new_entry.timeslot.end_time):
                return True

        return False

    @staticmethod
    def room_clash(existing_entries, new_entry) -> bool:
        new_day = normalize_day(new_entry.timeslot.day)

        for e in existing_entries:
            if e.room != new_entry.room:
                continue

            if normalize_day(e.timeslot.day) != new_day:
                continue

            if is_overlap(e.timeslot.start_time, e.timeslot.end_time,
                          new_entry.timeslot.start_time, new_entry.timeslot.end_time):
                return True

        return False

    @staticmethod
    def validate_no_clashes(existing_entries, new_entry) -> List[str]:
        """
        Returns list of clash messages. Empty list means no clashes.
        """
        errors: List[str] = []

        if ClashService.lecturer_clash(existing_entries, new_entry):
            errors.append("Lecturer clash detected: lecturer has an overlapping timeslot.")

        if ClashService.room_clash(existing_entries, new_entry):
            errors.append("Room clash detected: room is already booked in that timeslot.")

        return errors
