from __future__ import annotations

from typing import List
from models.timetable_entry import TimetableEntry


class ExportService:
    """
    Handles exporting timetable entries to a text file.
    """

    def export_to_text(self, entries: List[TimetableEntry], file_path: str) -> None:
        with open(file_path, "w", encoding="utf-8") as f:
            if not entries:
                return

            for e in entries:
                line = (
                    f"{e.course.code},"
                    f"{e.course.course_id},"
                    f"{e.lecturer.lecturer_id},"
                    f"{e.room},"
                    f"{e.timeslot.day},"
                    f"{e.timeslot.start_time}-"
                    f"{e.timeslot.end_time}\n"
                )
                f.write(line)


# ================================
# FUNCTIONAL WRAPPER (CRITICAL)
# ================================

def export_timetable(entries: List[TimetableEntry], file_path: str) -> None:
    """
    Wrapper required for Black-box, White-box, and Branch Coverage tests.
    """
    service = ExportService()
    service.export_to_text(entries, file_path)
