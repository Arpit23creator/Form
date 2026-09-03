class Student:
    def __init__(self, Name, Roll_no, marks, attendance):
        self.__Name = Name
        self.__Roll_no = Roll_no
        self.__marks = marks
        self.__attendance = attendance

    def get_Roll_no(self):
        return self.__Roll_no

    def display_student_info(self):
        return f"{self.__Name}, {self.__Roll_no}, {self.__marks}, {self.__attendance}"

    def calculate_percentage(self):
        return sum(self.__marks)/len(self.__marks)

    def check_result(self):
        if self.calculate_percentage() > 40:
            return "Pass"
        else:
            return "Fail"




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

students = []

students.append(student1)

students.append(student2)

students.append(student3)

students.append(student4)

students.append(student5)

students.append(student6)

students.append(student7)

students.append(student8)

students.append(student9)

students.append(student10)

students.extend([
    student11,
    student12,
    student13,
    student14,
    student15,
    student16,
    student17,
    student18,
    student19,
    student20,
    student21,
    student22,
    student23,
    student24,
    student25,
    student26,
    student27,
    student28,
    student29,
    student30
])


print('''
                                                    ========================================\n
                                          
                                                          STUDENT MANAGEMENT SYSTEM\n
                                          
                                                    ========================================

     ''')



print('''
1. Display All Students
2. Search Student
3. Add Student
4. Delete Student
5. View Student Result
6. Class Statistics
7. Exit
''')


choice = input("Enter your choice: ")

if(choice == "1"):
    for student in students:
        print(student.display_student_info())


elif(choice == "2"):
    Roll_no = int(input("Enter student's Roll_no: "))
    for student in students:
        if(student.get_Roll_no() == Roll_no):
            print(student.display_student_info())


elif(choice == "3"):
    print("Enter Student data: ")
    Name = input("Enter Student's name: ")
    Roll_Number = int(input("Enter Roll_no: "))
    Marks = []
    n = 4
    while(n > 0):
        Marks.append(int(input("Enter student's marks: ")))
        n -= 1
    Attendance = int(input("Enter student's attendance: "))
    new_student = Student(Name, Roll_Number, Marks, Attendance)
    students.append(new_student)

elif(choice == "4"):
    roll_no  = int(input("Enter Student's Roll_no: "))
    for student in students:
        if(student.get_Roll_no() == roll_no):
            students.remove(student)
    print("Student deleted successfully")

elif(choice == "5"):
    Roll = int(input("Enter Student's Roll_no: "))
    for student in students:
        if(student.get_Roll_no() == Roll):
            print(student.display_student_info())









    

        