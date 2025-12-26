from services.timetable_view_service import TimetableViewService

def print_entries(entries):
    for e in entries:
        print(
            e.course.code,
            e.lecturer.name,
            e.room,
            e.timeslot.day,
            e.timeslot.start_time,
            e.timeslot.end_time
        )
