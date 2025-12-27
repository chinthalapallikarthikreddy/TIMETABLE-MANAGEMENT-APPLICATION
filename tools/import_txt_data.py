import sys
sys.path.append("src")

from storage.data_context import DataContext
from storage.json_store import JsonStore
from storage.model_factory import ModelFactory

from models.course import Course
from models.lecturer import Lecturer
from models.timeslot import Timeslot
from models.timetable_entry import TimetableEntry


DATA_DIR = "data"
STORE_FILE = "data/store.json"


def import_courses(ctx):
    with open(f"{DATA_DIR}/courses.txt", "r") as f:
        for line in f:
            cid, name, code, level = line.strip().split(",")
            ctx.courses[cid] = Course(cid, name, code, int(level))


def import_lecturers(ctx):
    with open(f"{DATA_DIR}/lecturers.txt", "r") as f:
        for line in f:
            lid, name, email = line.strip().split(",")
            ctx.lecturers[lid] = Lecturer(lid, name, email)


def import_rooms(ctx):
    with open(f"{DATA_DIR}/rooms.txt", "r") as f:
        for line in f:
            room = line.strip()
            if room:
                ctx.rooms[room] = {"room_id": room}


def import_timetable(ctx):
    with open(f"{DATA_DIR}/timetable.txt", "r") as f:
        for line in f:
            course_id, lecturer_id, room, day, start, end = line.strip().split(",")

            entry = TimetableEntry(
                course=ctx.courses[course_id],
                lecturer=ctx.lecturers[lecturer_id],
                room=room,
                timeslot=Timeslot(day, start, end)
            )
            ctx.entries.append(entry)


def main():
    ctx = DataContext()
    store = JsonStore(STORE_FILE)

    import_courses(ctx)
    import_lecturers(ctx)
    import_rooms(ctx)
    import_timetable(ctx)

    store.save(ctx)
    print("Data imported successfully into store.json")


if __name__ == "__main__":
    main()
