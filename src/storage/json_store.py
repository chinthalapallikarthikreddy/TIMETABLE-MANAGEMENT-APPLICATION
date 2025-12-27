import json
from typing import Any, Dict

from storage.data_context import DataContext


class JsonStore:
    """
    File-based persistence using JSON.
    No database. Suitable for CO7095.
    """

    def __init__(self, filepath: str):
        self.filepath = filepath

    def save(self, ctx: DataContext) -> None:
        data = {
            "courses": {cid: c.to_dict() for cid, c in ctx.courses.items()},
            "lecturers": {lid: l.to_dict() for lid, l in ctx.lecturers.items()},
            "rooms": ctx.rooms,  # simple dictionary
            "entries": [self._entry_to_dict(e) for e in ctx.entries],
        }

        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load(self, ctx: DataContext, model_factory: "ModelFactory") -> None:
        """
        model_factory creates model objects from dictionaries.
        This avoids circular dependencies and keeps code testable.

        model_factory must provide:
        - course_from_dict(d)
        - lecturer_from_dict(d)
        - timeslot_from_dict(d)
        - entry_from_dict(d, courses_by_id, lecturers_by_id)
        """
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            # No data yet, treat as empty store
            return

        ctx.clear()

        courses_raw: Dict[str, Dict[str, Any]] = data.get("courses", {})
        lecturers_raw: Dict[str, Dict[str, Any]] = data.get("lecturers", {})
        rooms_raw: Dict[str, Any] = data.get("rooms", {})
        entries_raw = data.get("entries", [])

        for cid, cdict in courses_raw.items():
            ctx.courses[cid] = model_factory.course_from_dict(cdict)

        for lid, ldict in lecturers_raw.items():
            ctx.lecturers[lid] = model_factory.lecturer_from_dict(ldict)

        ctx.rooms = rooms_raw

        for edict in entries_raw:
            entry = model_factory.entry_from_dict(edict, ctx.courses, ctx.lecturers)
            ctx.entries.append(entry)

    @staticmethod
    def _entry_to_dict(entry) -> Dict[str, Any]:
        """
        TimetableEntry contains Course and Lecturer objects, so store IDs and timeslot data.
        """
        return {
            "course_id": entry.course.course_id,
            "lecturer_id": entry.lecturer.lecturer_id,
            "room": entry.room,
            "timeslot": entry.timeslot.to_dict(),
        }
