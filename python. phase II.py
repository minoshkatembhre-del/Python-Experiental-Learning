import json

FILE = "students.json"


def load_students():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_students(students):
    with open(FILE, "w") as file:
        json.dump(students, file, indent=4)


def calculate_result(m1, m2, m3):
    total = m1 + m2 + m3
    percentage = (total / 300) * 100

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    if percentage >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    return total, percentage, grade, result


def add_student():
    students = load_students()

    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    m1 = int(input("Enter marks of Subject 1: "))
    m2 = int(input("Enter marks of Subject 2: "))
    m3 = int(input("Enter marks of Subject 3: "))

    total, percentage, grade, result = calculate_result(m1, m2, m3)

    student = {
        "roll_no": roll_no,
        "name": name,
        "subject1": m1,
        "subject2": m2,
        "subject3": m3,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "result": result
    }

    students.append(student)
    save_students(students)

    print("\nStudent record added successfully.")


def view_students():
    students = load_students()

    if not students:
        print("\nNo student records found.")
        return

    print("\n----- STUDENT RECORDS -----")

    for student in students:
        print("Roll No:", student["roll_no"])
        print("Name:", student["name"])
        print("Total:", student["total"])
        print("Percentage:", student["percentage"])
        print("Grade:", student["grade"])
        print("Result:", student["result"])
        print("--------------------------")


def search_student():
    students = load_students()

    roll_no = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found")
            print("Name:", student["name"])
            print("Total:", student["total"])
            print("Percentage:", student["percentage"])
            print("Grade:", student["grade"])
            print("Result:", student["result"])
            return

    print("\nStudent not found.")


def update_student():
    students = load_students()

    roll_no = input("Enter Roll Number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:

            student["name"] = input("Enter new name: ")
            student["subject1"] = int(input("Enter new marks of Subject 1: "))
            student["subject2"] = int(input("Enter new marks of Subject 2: "))
            student["subject3"] = int(input("Enter new marks of Subject 3: "))

            total, percentage, grade, result = calculate_result(
                student["subject1"],
                student["subject2"],
                student["subject3"]
            )

            student["total"] = total
            student["percentage"] = percentage
            student["grade"] = grade
            student["result"] = result

            save_students(students)

            print("\nStudent record updated successfully.")
            return

    print("\nStudent not found.")


def delete_student():
    students = load_students()

    roll_no = input("Enter Roll Number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            save_students(students)
            print("\nStudent record deleted successfully.")
            return

    print("\nStudent not found.")


def generate_result():
    students = load_students()

    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["roll_no"] == roll_no:

            print("\n===== STUDENT RESULT =====")
            print("Roll Number:", student["roll_no"])
            print("Student Name:", student["name"])
            print("Subject 1:", student["subject1"])
            print("Subject 2:", student["subject2"])
            print("Subject 3:", student["subject3"])
            print("Total Marks:", student["total"])
            print("Percentage:", student["percentage"])
            print("Grade:", student["grade"])
            print("Result:", student["result"])
            print("==========================")

            return

    print("\nStudent not found.")


while True:

    print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Generate Result")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        generate_result()

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")