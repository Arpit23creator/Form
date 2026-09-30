class Student:
    def __init__(self, Name, Roll_no, marks, attendance):
        self.__Name = Name
        self.__Roll_no = Roll_no
        self.__marks = marks
        self.__attendance = attendance

    def get_Roll_no(self):
        return self.__Roll_no

    def display_student_info(self):
        return f"Name: {self.__Name}, Roll No: {self.__Roll_no}, Marks: {self.__marks}, Attendance: {self.__attendance}%"

    def calculate_percentage(self):
        if not self.__marks:          
            return 0
        return sum(self.__marks) / len(self.__marks)

    def check_result(self):
        if self.calculate_percentage() >= 40:
            return "Pass"
        else:
            return "Fail"

def get_int_input(prompt, min_val=None, max_val=None):
    while True:
        value = input(prompt)
        try:
            value = int(value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if min_val is not None and value < min_val:
            print(f"Value must be at least {min_val}.")
            continue
        if max_val is not None and value > max_val:
            print(f"Value must be at most {max_val}.")
            continue

        return value


# ---------------- STUDENT DATA ----------------

student1 = Student("Lavi", 101, [93, 89, 96, 94], 97)
student2 = Student("Rahul", 102, [72, 65, 81, 75], 76)
student3 = Student("Aman", 103, [45, 52, 48, 60], 69)
student4 = Student("Priya", 104, [65, 74, 70, 68], 76)
student5 = Student("Rohan", 105, [55, 62, 58, 64], 72)
student6 = Student("Khushi", 106, [88, 91, 84, 87], 91)
student7 = Student("Vikas", 107, [45, 52, 48, 55], 68)
student8 = Student("Simran", 108, [76, 83, 79, 81], 85)
student9 = Student("Karan", 109, [38, 45, 42, 50], 74)
student10 = Student("Arpit", 110, [85, 78, 92, 80], 88)

student11 = Student("Aditya", 111, [82, 76, 89, 85], 84)
student12 = Student("Nisha", 112, [74, 68, 81, 77], 79)
student13 = Student("Yash", 113, [91, 87, 93, 89], 92)
student14 = Student("Pooja", 114, [63, 71, 67, 75], 73)
student15 = Student("Mohit", 115, [56, 64, 59, 61], 81)
student16 = Student("Ishita", 116, [88, 85, 90, 92], 95)
student17 = Student("Varun", 117, [42, 48, 55, 51], 69)
student18 = Student("Riya", 118, [79, 84, 76, 82], 87)
student19 = Student("Sahil", 119, [68, 73, 65, 70], 78)
student20 = Student("Tanya", 120, [94, 91, 88, 95], 97)

student21 = Student("Kunal", 121, [51, 58, 62, 55], 71)
student22 = Student("Sneha", 122, [86, 79, 91, 84], 89)
student23 = Student("Deepak", 123, [39, 44, 47, 42], 66)
student24 = Student("Mehak", 124, [72, 77, 69, 74], 82)
student25 = Student("Rajat", 125, [83, 88, 80, 85], 91)
student26 = Student("Muskan", 126, [61, 67, 73, 65], 76)
student27 = Student("Harsh", 127, [90, 94, 87, 92], 93)
student28 = Student("Komal", 128, [47, 53, 49, 56], 70)
student29 = Student("Nitin", 129, [75, 71, 78, 80], 85)
student30 = Student("Shivani", 130, [89, 93, 86, 90], 94)


students = [
    student1, student2, student3, student4, student5,
    student6, student7, student8, student9, student10,
    student11, student12, student13, student14, student15,
    student16, student17, student18, student19, student20,
    student21, student22, student23, student24, student25,
    student26, student27, student28, student29, student30
]


# ---------------- MENU ----------------

while True:

    print("\n========================================")
    print("        STUDENT MANAGEMENT SYSTEM")
    print("========================================")

    print("\n1. Display All Students")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Delete Student")
    print("5. View Student Result")
    print("6. Class Statistics")
    print("7. Exit")

    choice = input("\nEnter your choice: ")


    # ---------------- OPTION 1 ----------------

    if choice == "1":

        print("\n========== ALL STUDENTS ==========")

        if len(students) == 0:
            print("No students available.")

        else:
            for student in students:
                print(student.display_student_info())


    # ---------------- OPTION 2 ----------------

    elif choice == "2":

        Roll_no = get_int_input("Enter student's Roll_no: ")   

        found = False

        for student in students:

            if student.get_Roll_no() == Roll_no:
                print("\nStudent Found!")
                print(student.display_student_info())
                found = True
                break

        if not found:
            print("Student not found.")


    # ---------------- OPTION 3 ----------------

    elif choice == "3":

        print("\n========== ADD STUDENT ==========")

        Name = input("Enter Student's name: ").strip()

        while not Name:   
            print("Name cannot be empty.")
            Name = input("Enter Student's name: ").strip()

        Roll_Number = get_int_input("Enter Roll_no: ")   

        duplicate = False

        for student in students:

            if student.get_Roll_no() == Roll_Number:
                duplicate = True
                break

        if duplicate:
            print("A student with this Roll_no already exists.")

        else:

            Marks = []

            print("Enter marks of 4 subjects:")

            n = 4

            while n > 0:

                mark = get_int_input("Enter student's marks: ")  

                if 0 <= mark <= 100:
                    Marks.append(mark)
                    n -= 1

                else:
                    print("Marks must be between 0 and 100.")

            Attendance = get_int_input("Enter student's attendance: ")   

            if 0 <= Attendance <= 100:

                new_student = Student(
                    Name,
                    Roll_Number,
                    Marks,
                    Attendance
                )

                students.append(new_student)

                print("Student added successfully.")

            else:
                print("Attendance must be between 0 and 100.")


    # ---------------- OPTION 4 ----------------

    elif choice == "4":

        roll_no = get_int_input("Enter Student's Roll_no: ")   

        found = False

        for student in list(students):

            if student.get_Roll_no() == roll_no:

                students.remove(student)

                print("Student deleted successfully.")

                found = True

                break

        if not found:
            print("Student not found.")


    # ---------------- OPTION 5 ----------------

    elif choice == "5":

        Roll = get_int_input("Enter Student's Roll_no: ")   

        found = False

        for student in students:

            if student.get_Roll_no() == Roll:

                print("\n========== STUDENT RESULT ==========")

                print(student.display_student_info())

                percentage = student.calculate_percentage()

                print(f"Percentage: {percentage:.2f}%")

                print(f"Result: {student.check_result()}")

                found = True

                break

        if not found:
            print("Student not found.")


    # ---------------- OPTION 6 ----------------

    elif choice == "6":

        if len(students) == 0:

            print("No students available.")

        else:

            total_percentage = 0
            passed = 0
            failed = 0

            highest_percentage = students[0].calculate_percentage()
            lowest_percentage = students[0].calculate_percentage()

            highest_student = students[0]
            lowest_student = students[0]

            for student in students:

                percentage = student.calculate_percentage()

                total_percentage += percentage

                if student.check_result() == "Pass":
                    passed += 1

                else:
                    failed += 1

                if percentage > highest_percentage:
                    highest_percentage = percentage
                    highest_student = student

                if percentage < lowest_percentage:
                    lowest_percentage = percentage
                    lowest_student = student


            class_average = total_percentage / len(students)

            print("\n========== CLASS STATISTICS ==========")

            print(f"Total Students: {len(students)}")

            print(f"Class Average: {class_average:.2f}%")

            print(f"Passed Students: {passed}")

            print(f"Failed Students: {failed}")

            print(
                f"Highest Percentage: "
                f"{highest_percentage:.2f}% "
                f"({highest_student.get_Roll_no()})"
            )

            print(
                f"Lowest Percentage: "
                f"{lowest_percentage:.2f}% "
                f"({lowest_student.get_Roll_no()})"
            )


    # ---------------- OPTION 7 ----------------

    elif choice == "7":

        print("\nThank you for using Student Management System!")
        break


    # ---------------- INVALID OPTION ----------------

    else:

        print("Invalid choice. Please enter a number from 1 to 7.")