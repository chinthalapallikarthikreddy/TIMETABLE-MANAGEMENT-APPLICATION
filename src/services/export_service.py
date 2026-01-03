from models.timetable_entry import TimetableEntry


def parse_time_to_minutes(t: str) -> int:
    h, m = t.split(":")
    return int(h) * 60 + int(m)


def normalize_day(day: str) -> str:
    return day.strip().lower()


def day_to_index(day: str) -> int:
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    return days.index(normalize_day(day))


class ExportService:
    """
    Handles exporting timetable entries to a text file.
    """

    def export_to_text(self, entries, file_path: str) -> None:
        with open(file_path, "w") as f:
            if not entries:
                f.write("")
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

def export_timetable(entries, file_path: str) -> None:
    """
    Wrapper required for Black-box, White-box, and Branch Coverage tests.
    """
    service = ExportService()
    return service.export_to_text(entries, file_path)
