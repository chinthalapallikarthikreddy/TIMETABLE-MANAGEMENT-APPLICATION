import random

DATA_DIR = "data"

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
TIMES = [
    ("09:00", "10:00"),
    ("10:00", "11:00"),
    ("11:00", "12:00"),
    ("13:00", "14:00"),
    ("14:00", "15:00"),
    ("15:00", "16:00"),
]

def generate_courses():
    courses = []
    for i in range(1, 16):  # 15 courses
        courses.append(f"C{i:03},Course_{i},CO7{i:03},7")
    return courses

def generate_lecturers():
    lecturers = []
    for i in range(1, 13):  # 12 lecturers
        lecturers.append(f"L{i:03},Dr Lecturer {i},lecturer{i}@uni.ac.uk")
    return lecturers

def generate_rooms():
    return [f"R{i:03}" for i in range(101, 111)]  # 10 rooms

def generate_timetable(courses, lecturers, rooms):
    entries = []
    used_slots = set()

    while len(entries) < 40:  # 40 timetable entries
        course = random.choice(courses).split(",")[0]
        lecturer = random.choice(lecturers).split(",")[0]
        room = random.choice(rooms)
        day = random.choice(DAYS)
        start, end = random.choice(TIMES)

        key = (lecturer, room, day, start)
        if key in used_slots:
            continue

        used_slots.add(key)
        entries.append(f"{course},{lecturer},{room},{day},{start},{end}")

    return entries

def write_file(filename, lines):
    with open(f"{DATA_DIR}/{filename}", "w") as f:
        for line in lines:
            f.write(line + "\n")

def main():
    courses = generate_courses()
    lecturers = generate_lecturers()
    rooms = generate_rooms()
    timetable = generate_timetable(courses, lecturers, rooms)

    write_file("courses.txt", courses)
    write_file("lecturers.txt", lecturers)
    write_file("rooms.txt", rooms)
    write_file("timetable.txt", timetable)

    print("Bulk data generated:")
    print(f"- {len(courses)} courses")
    print(f"- {len(lecturers)} lecturers")
    print(f"- {len(rooms)} rooms")
    print(f"- {len(timetable)} timetable entries")

if __name__ == "__main__":
    main()
