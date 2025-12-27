from dataclasses import dataclass, field
from typing import Dict, List

# These are expected from Member 1
# Course has: course_id, name, code, level
# Lecturer has: lecturer_id, name, email
# Timeslot has: day, start_time, end_time
# TimetableEntry has: course, lecturer, room, timeslot


@dataclass
class DataContext:
    courses: Dict[str, object] = field(default_factory=dict)     # key: course_id
    lecturers: Dict[str, object] = field(default_factory=dict)   # key: lecturer_id
    rooms: Dict[str, object] = field(default_factory=dict)       # key: room_id or room_code
    entries: List[object] = field(default_factory=list)          # list of TimetableEntry

    def clear(self) -> None:
        self.courses.clear()
        self.lecturers.clear()
        self.rooms.clear()
        self.entries.clear()
