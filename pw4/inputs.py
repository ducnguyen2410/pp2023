from domains import Student, Course
from outputs import Output

class Input(Student, Course,Output):
    s_list = Student(0,0,0)
    c_list = Course(0,0,0)

    def __init__(self, str):
        if str == "student":
            self.Student_info()
        elif str == "course":
            self.Course_info()
    
    def Student_info(self):
        id = input("Enter student ID: ")
        if self.s_list.in_list(int(id)):
            print("ID already in list!")
        else:
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            self.s_list = Student(id, name, dob)
            
            
    def Course_info(self):
        id = input("Enter the course ID: ")
        if self.c_list.in_list(id):
            print("ID already in list.")
        else:
            name = input("Enter the course name: ")
            ect = input("Enter the course ECT: ")
            self.c_list = Course(id, name, ect)
            
    def Enter_grade(self):
        id = input("Enter the student ID to enter grade: ")
        if not self.s_list.in_list(int(id)):
            print("Student ID not found!")
        else:
            c_id = input("Which course do you want to grade this student: ")
            if not self.c_list.in_list(int(c_id)):
                print("Course not in the list!")
            else:
                score = input("Enter the student's grade: ")
                while not score.isdecimal() and not score.isdigit():
                    score = input("Invalid score. Please type again: ")
                self.s_list.total[int(id)]["grade"][int(c_id)] = score
                    
                