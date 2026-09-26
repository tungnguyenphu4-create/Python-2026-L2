
def input_number_of_students():
    """Ask the user how many students are in the class."""
    while True:
        try:
            n = int(input("Enter the number of students in the class: "))
            if n < 0:
                print("Please enter a non-negative number.")
                continue
            return n
        except ValueError:
            print("Invalid input. Please enter an integer.")


def input_students(n):
    """Input id, name and date of birth for n students. Returns a list of dicts."""
    students = []
    for i in range(n):
        print(f"\n-- Student {i + 1} --")
        sid = input("  Student ID: ").strip()
        name = input("  Name: ").strip()
        dob = input("  Date of birth (dd/mm/yyyy): ").strip()
        students.append({"id": sid, "name": name, "dob": dob})
    return students


def input_number_of_courses():
    """Ask the user how many courses to enter."""
    while True:
        try:
            n = int(input("Enter the number of courses: "))
            if n < 0:
                print("Please enter a non-negative number.")
                continue
            return n
        except ValueError:
            print("Invalid input. Please enter an integer.")


def input_courses(n):
    """Input id and name for n courses. Returns a list of dicts."""
    courses = []
    for i in range(n):
        print(f"\n-- Course {i + 1} --")
        cid = input("  Course ID: ").strip()
        cname = input("  Course name: ").strip()
        courses.append({"id": cid, "name": cname})
    return courses


def find_course(courses):
    """Let the user pick a course by ID. Returns the matching course dict or None."""
    list_courses(courses)
    cid = input("Enter the course ID to select: ").strip()
    for c in courses:
        if c["id"] == cid:
            return c
    print("No course found with that ID.")
    return None


def input_marks_for_course(courses, students, marks):
    """
    Select a course and input a mark for every student in that course.
    'marks' is a dict of the form: {course_id: {student_id: mark}}
    """
    if not courses:
        print("No courses available. Please input courses first.")
        return
    if not students:
        print("No students available. Please input students first.")
        return

    course = find_course(courses)
    if course is None:
        return

    course_marks = marks.setdefault(course["id"], {})
    print(f"\nEntering marks for course '{course['name']}' ({course['id']}):")
    for s in students:
        while True:
            try:
                mark = float(input(f"  Mark for {s['name']} ({s['id']}): "))
                break
            except ValueError:
                print("  Invalid mark. Please enter a number.")
        course_marks[s["id"]] = mark


def list_courses(courses):
    """Print all courses."""
    if not courses:
        print("No courses to display.")
        return
    print("\n=== List of courses ===")
    print(f"{'ID':<10}{'Name':<30}")
    print("-" * 40)
    for c in courses:
        print(f"{c['id']:<10}{c['name']:<30}")


def list_students(students):
    """Print all students."""
    if not students:
        print("No students to display.")
        return
    print("\n=== List of students ===")
    print(f"{'ID':<10}{'Name':<25}{'DoB':<15}")
    print("-" * 50)
    for s in students:
        print(f"{s['id']:<10}{s['name']:<25}{s['dob']:<15}")


def show_marks_for_course(courses, students, marks):
    """Show all student marks for a chosen course."""
    if not courses:
        print("No courses available.")
        return

    course = find_course(courses)
    if course is None:
        return

    course_marks = marks.get(course["id"], {})
    print(f"\n=== Marks for course '{course['name']}' ({course['id']}) ===")
    if not course_marks:
        print("No marks entered for this course yet.")
        return

    print(f"{'ID':<10}{'Name':<25}{'Mark':<8}")
    print("-" * 43)
    id_to_name = {s["id"]: s["name"] for s in students}
    for sid, mark in course_marks.items():
        name = id_to_name.get(sid, "(unknown)")
        print(f"{sid:<10}{name:<25}{mark:<8}")


def print_menu():
    print("\n========== STUDENT MARK MANAGEMENT ==========")
    print("1. Input number of students & student info")
    print("2. Input number of courses & course info")
    print("3. Select a course and input marks")
    print("4. List courses")
    print("5. List students")
    print("6. Show student marks for a course")
    print("0. Exit")
    print("===============================================")


def main():
    students = []
    courses = []
    marks = {}  # {course_id: {student_id: mark}}

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            n = input_number_of_students()
            students = input_students(n)
        elif choice == "2":
            n = input_number_of_courses()
            courses = input_courses(n)
        elif choice == "3":
            input_marks_for_course(courses, students, marks)
        elif choice == "4":
            list_courses(courses)
        elif choice == "5":
            list_students(students)
        elif choice == "6":
            show_marks_for_course(courses, students, marks)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()