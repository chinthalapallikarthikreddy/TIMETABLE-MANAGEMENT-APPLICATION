import os

from storage.data_context import DataContext
from storage.json_store import JsonStore
from storage.model_factory import ModelFactory

from services.clash_service import ClashService
from services.search_service import SearchService
from services.export_service import ExportService

from models.course import Course
from models.lecturer import Lecturer
from models.timeslot import Timeslot
from models.timetable_entry import TimetableEntry


STORE_FILE = "data/store.json"


def main_menu():
    print("\n=== Timetable Management System ===")
    print("1. Add course")
    print("2. Add lecturer")
    print("3. Add timetable entry")
    print("4. View next class")
    print("5. Find free rooms")
    print("6. Export timetable")
    print("0. Exit")


def main():
    ctx = DataContext()

    # -------------------------------
    # Auto-load persisted data safely
    # -------------------------------
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    store_path = os.path.join(project_root, STORE_FILE)

    store = JsonStore(store_path)
    factory = ModelFactory()

    if os.path.exists(store_path):
        try:
            store.load(ctx, factory)
            # Optional debug line (comment out for video)
            # print(f"Loaded {len(ctx.entries)} timetable entries")
        except Exception as ex:
            print(f"Warning: could not load saved data: {ex}")

    while True:
        main_menu()
        choice = input("Select option: ").strip()

        # -------------------------------
        # Add course
        # -------------------------------
        if choice == "1":
            c = Course(
                course_id=input("Course ID: "),
                name=input("Name: "),
                code=input("Code: "),
                level=int(input("Level: "))
            )
            ctx.courses[c.course_id] = c
            store.save(ctx)

        # -------------------------------
        # Add lecturer
        # -------------------------------
        elif choice == "2":
            l = Lecturer(
                lecturer_id=input("Lecturer ID: "),
                name=input("Name: "),
                email=input("Email: ")
            )
            ctx.lecturers[l.lecturer_id] = l
            store.save(ctx)

        # -------------------------------
        # Add timetable entry
        # -------------------------------
        elif choice == "3":
            course_id = input("Course ID: ")
            lecturer_id = input("Lecturer ID: ")
            room = input("Room: ")
            day = input("Day: ")
            start = input("Start time (HH:MM): ")
            end = input("End time (HH:MM): ")

            entry = TimetableEntry(
                course=ctx.courses[course_id],
                lecturer=ctx.lecturers[lecturer_id],
                room=room,
                timeslot=Timeslot(day, start, end)
            )

            errors = ClashService.validate_no_clashes(ctx.entries, entry)
            if errors:
                for e in errors:
                    print("ERROR:", e)
            else:
                ctx.entries.append(entry)
                store.save(ctx)
                print("Timetable entry added.")

        # -------------------------------
        # View next class
        # -------------------------------
        elif choice == "4":
            day = input("Current day: ")
            time = input("Current time (HH:MM): ")

            next_entry = SearchService.next_class(ctx.entries, day, time)

            if next_entry:
                print(
                    "Next class:",
                    next_entry.course.code,
                    next_entry.timeslot.day,
                    next_entry.timeslot.start_time
                )
            else:
                print("No upcoming classes found.")

        # -------------------------------
        # Find free rooms
        # -------------------------------
        elif choice == "5":
            day = input("Day: ")
            start = input("Start time (HH:MM): ")
            end = input("End time (HH:MM): ")

            rooms = list(ctx.rooms.keys())
            free = SearchService.find_free_rooms(ctx.entries, rooms, day, start, end)
            print("Free rooms:", free)

        # -------------------------------
        # Export timetable
        # -------------------------------
        elif choice == "6":
            ExportService().export_to_text(ctx.entries, "data/timetable_export.txt")
            print("Timetable exported.")

        # -------------------------------
        # Exit
        # -------------------------------
        elif choice == "0":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
