class TimetableViewService:

    @staticmethod
    def view_by_day(entries, day):
        return sorted(
            [e for e in entries if e.timeslot.day.lower() == day.lower()],
            key=lambda x: x.timeslot.start_time
        )

    @staticmethod
    def view_by_week(entries):
        timetable = {}
        for entry in entries:
            day = entry.timeslot.day
            timetable.setdefault(day, []).append(entry)

        for day in timetable:
            timetable[day] = sorted(
                timetable[day],
                key=lambda x: x.timeslot.start_time
            )
        return timetable

    @staticmethod
    def filter_by_course(entries, course_code):
        return [e for e in entries if e.course.code == course_code]

    @staticmethod
    def filter_by_lecturer(entries, lecturer_id):
        return [e for e in entries if e.lecturer.lecturer_id == lecturer_id]
