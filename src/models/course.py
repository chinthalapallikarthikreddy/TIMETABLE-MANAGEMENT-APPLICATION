class Course:
    def __init__(self, course_id, name, code, level):
        self.course_id = course_id
        self.name = name
        self.code = code
        self.level = level
        self.validate()

    def validate(self):
        if not self.course_id or not self.code:
            raise ValueError("Course ID and code are required")
        if self.level <= 0:
            raise ValueError("Course level must be positive")

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "name": self.name,
            "code": self.code,
            "level": self.level
        }
