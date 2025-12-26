from typing import List
from utils.time_utils import day_to_index, parse_time_to_minutes, normalize_day


class ExportService:
    @staticmethod
    def export_to_text(entries, filepath: str) -> None:
        """
        Exports timetable entries to a text file in a readable format.
        """
        # Sort by day then start_time
        def sort_key(e):
            return (day_to_index(e.timeslot.day), parse_time_to_minutes(e.timeslot.start_time))

        entries_sorted = sorted(entries, key=sort_key)

        lines: List[str] = []
        lines.append("Timetable Export")
        lines.append("=" * 60)

        for e in entries_sorted:
            line = (
                f"{normalize_day(e.timeslot.day).title():<10} "
                f"{e.timeslot.start_time}-{e.timeslot.end_time} | "
                f"{e.course.code:<10} | "
                f"{e.lecturer.name:<20} | "
                f"Room: {e.room}"
            )
            lines.append(line)

        content = "\n".join(lines)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
