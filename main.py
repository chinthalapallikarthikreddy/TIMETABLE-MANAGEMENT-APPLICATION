from services.clash_service import ClashService
from services.search_service import SearchService
from services.export_service import ExportService

def main_menu():
    print("1. Add timetable entry")
    print("2. Find next class")
    print("3. Find free rooms")
    print("4. Export timetable")
    print("0. Exit")

def main():
    entries = []          # loaded from file later
    rooms = ["R101", "R102", "R103"]

    while True:
        main_menu()
        choice = input("Choose option: ")

        if choice == "1":
            # create new_entry using Member 1 models
            # call ClashService.validate_no_clashes()
            pass

        elif choice == "2":
            # call SearchService.next_class()
            pass

        elif choice == "3":
            # call SearchService.find_free_rooms()
            pass

        elif choice == "4":
            # call ExportService.export_to_text()
            pass

        elif choice == "0":
            break

if __name__ == "__main__":
    main()
