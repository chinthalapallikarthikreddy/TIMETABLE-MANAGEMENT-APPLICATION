import os
import tempfile

from storage.data_context import DataContext
from storage.json_store import JsonStore
from storage.model_factory import ModelFactory

from models.course import Course
from models.lecturer import Lecturer
from models.timeslot import Timeslot
from models.timetable_entry import TimetableEntry


def test_save_and_load_round_trip():
    ctx = DataContext()

    c1 = Course(course_id="C001", name="Software QA", code="CO7095", level=7)
    l1 = Lecturer(lecturer_id="L001", name="Dr A", email="a@uni.ac.uk")
    t1 = Timeslot(day="Monday", start_time="09:00", end_time="10:00")
    e1 = TimetableEntry(course=c1, lecturer=l1, room="R101", timeslot=t1)

    ctx.courses[c1.course_id] = c1
    ctx.lecturers[l1.lecturer_id] = l1
    ctx.rooms["R101"] = {"room_id": "R101"}
    ctx.entries.append(e1)

    with tempfile.TemporaryDirectory() as tmpdir:
        fp = os.path.join(tmpdir, "store.json")
        store = JsonStore(fp)

        store.save(ctx)

        ctx2 = DataContext()
        store.load(ctx2, ModelFactory())

        assert "C001" in ctx2.courses
        assert "L001" in ctx2.lecturers
        assert len(ctx2.entries) == 1
        assert ctx2.entries[0].room == "R101"
        assert ctx2.entries[0].course.code == "CO7095"
