from models.course import Course
from models.lecturer import Lecturer
from models.timeslot import Timeslot
from models.timetable_entry import TimetableEntry


class ModelFactory:
    @staticmethod
    def course_from_dict(d: dict) -> Course:
        return Course(
            course_id=d["course_id"],
            name=d["name"],
            code=d["code"],
            level=d["level"],
        )

    @staticmethod
    def lecturer_from_dict(d: dict) -> Lecturer:
        return Lecturer(
            lecturer_id=d["lecturer_id"],
            name=d["name"],
            email=d["email"],
        )

    @staticmethod
    def timeslot_from_dict(d: dict) -> Timeslot:
        return Timeslot(
            day=d["day"],
            start_time=d["start_time"],
            end_time=d["end_time"],
        )

    def entry_from_dict(self, d: dict, courses_by_id: dict, lecturers_by_id: dict) -> TimetableEntry:
        course_id = d["course_id"]
        lecturer_id = d["lecturer_id"]

        if course_id not in courses_by_id:
            raise ValueError(f"Saved entry references missing course_id: {course_id}")
        if lecturer_id not in lecturers_by_id:
            raise ValueError(f"Saved entry references missing lecturer_id: {lecturer_id}")

        timeslot = self.timeslot_from_dict(d["timeslot"])

        return TimetableEntry(
            course=courses_by_id[course_id],
            lecturer=lecturers_by_id[lecturer_id],
            room=d["room"],
            timeslot=timeslot,
        )
