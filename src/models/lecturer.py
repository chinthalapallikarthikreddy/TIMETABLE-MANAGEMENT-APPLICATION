class Lecturer:
    def __init__(self, lecturer_id, name, email):
        self.lecturer_id = lecturer_id
        self.name = name
        self.email = email
        self.validate()

    def validate(self):
        if "@" not in self.email:
            raise ValueError("Invalid lecturer email")

    def to_dict(self):
        return {
            "lecturer_id": self.lecturer_id,
            "name": self.name,
            "email": self.email
        }
