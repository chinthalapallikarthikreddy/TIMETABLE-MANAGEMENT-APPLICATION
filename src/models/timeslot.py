class Timeslot:
    def __init__(self, day, start_time, end_time):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.validate()

    def validate(self):
        if self.start_time >= self.end_time:
            raise ValueError("Start time must be before end time")

    def overlaps(self, other):
        if self.day != other.day:
            return False
        return not (self.end_time <= other.start_time or self.start_time >= other.end_time)

    def to_dict(self):
        return {
            "day": self.day,
            "start_time": self.start_time,
            "end_time": self.end_time
        }
