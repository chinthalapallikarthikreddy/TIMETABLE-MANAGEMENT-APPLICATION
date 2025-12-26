class TimetableEntry:
    def __init__(self, course, lecturer, room, timeslot):
        self.course = course
        self.lecturer = lecturer
        self.room = room
        self.timeslot = timeslot

    def to_dict(self):
        return {
            "course": self.course.to_dict(),
            "lecturer": self.lecturer.to_dict(),
            "room": self.room,
            "timeslot": self.timeslot.to_dict()
        }
