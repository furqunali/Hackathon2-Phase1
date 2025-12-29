# main.py - In-Memory Student Management System
import os

def main():
    students = []  # Data is stored in RAM and resets on exit

    while True:
        print("\n--- 🎓 STUDENT SYSTEM (PHASE 1) ---")
        print("1. Add Student\n2. View Students & GPA\n3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter Name: ")
            sid = input("Enter ID: ")
            students.append({"id": sid, "name": name, "grades": [85, 90]}) # Dummy grades for demo
            print(f"✅ Added {name}!")

        elif choice == '2':
            print("\nID | Name | GPA")
            for s in students:
                gpa = sum(s['grades']) / len(s['grades']) if s['grades'] else 0
                print(f"{s['id']} | {s['name']} | {gpa:.2f}")

        elif choice == '3':
            print("Exiting... Memory cleared.")
            break

if __name__ == "__main__":
    main()