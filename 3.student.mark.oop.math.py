import curses
from curses import wrapper
import math
import numpy

class Student:
    total = {}
    total_count = 0
    
    def in_list(self,id):
        if id not in self.total:
            return False
        return True
    
    def __init__(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0,2,"""
        You chose to fill in student's information.
        Press any key to continue.""")
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()
        curses.endwin()
        id = input("\nEnter student id: ")
        if self.in_list(id):
            print("Student already in list!")
        else:
            name = input("Enter student name: ")
            dob = input("Enter student's date of birth in format: dd/mm/yyyy: ")
            temp = [name, dob]
            self.total[str(id)] = temp
            self.total_count += 1
        
    def get_name(self, id):
        return self.total[str(id)][0]
    
    def get_dob(self, id):
        return self.total[str(id)][1]
    
    def get_list(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0,2,"""
        You chose to get list of all students' information.
        Press any key to continue.""")
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()
        curses.endwin()
        for i in self.total:
            stdscr.addstr("\n")
            stdscr.addstr("Student id: " + i)
            stdscr.addstr(",Student name: " + self.get_name(i))
            stdscr.addstr(",Student date of birth: " + self.get_dob(i)+ ".")
            stdscr.addstr("\n")
        stdscr.getch()
    
class Course(Student):
    total = {}
    total_count = 0
    
    def in_list(self, id):
        if id in self.total:
            return True
        return False
    
    def __init__(self,stdscr):
        stdscr.clear()
        stdscr.addstr(0,2,"""
        You chose to fill in course's information.
        Press any key to continue.""")
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()
        curses.endwin()
        id = int(input("\nEnter a course's id: "))
        if self.in_list(id):
            print("ID already exist.")
        else:
            name = input("Enter the course's name: ")
            ect = input("Enter number of credits this course has: ")
            self.total[id] = [name, ect]
    
    def get_name(self, id):
        return self.total[id][0]
    
    def enter_grade(self, student_list: Student, stdscr):
        grade_list = []
        each = {}
        stdscr.clear()
        stdscr.addstr(0,2,"""
        You chose to fill in student's score.
        Press any key to continue.""")
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()
        curses.endwin()
        id = input("\nEnter course ID that you want to enter grade: ")
        if int(id) not in self.total or len(self.total[int(id)]) == 3:
            print("ID not available or not in the list")
        else:
            print("Course: " + self.get_name(int(id)))
            for i in super().total:
                print("\n")
                print("Student ID: " + i)
                print("Student name: " + student_list.get_name(str(i)))
                print("Student date of birth: " + student_list.get_dob(i))
                score = float(input("Enter the score of this student: "))
                each[i] = math.floor(score * 10) / 10
            grade_list = each
            self.total[int(id)].append(grade_list)
        
    def get_grade(self, student_list: Student, stdscr):
        stdscr.clear()
        stdscr.addstr(0,2,"""
        You chose to get students'grade from a course.
        Press any key to continue.""")
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()
        curses.endwin()
        id = int(input("\nEnter the course id that you want to show grade: "))
        if id not in self.total:
            stdscr.addstr("ID not found")
        elif len(self.total[int(id)]) == 2:
            stdscr.addstr("Grade is not updated!")
        else:
            stdscr.addstr("Course: " + self.total[id][0])
            stdscr.addstr("\n")
            for i in self.total[int(id)][2]:
                stdscr.addstr("\n")
                stdscr.addstr("Student ID: " + str(i))
                stdscr.addstr("\n")
                stdscr.addstr("Student's name: " + student_list.total[str(i)][0])
                stdscr.addstr("\n")
                stdscr.addstr("Student's date of birth: " + student_list.total[str(i)][1])
                stdscr.addstr("\n")
                stdscr.addstr("Grade: " + str(self.total[int(id)][2][i]) + ".")
                stdscr.addstr("\n")
        stdscr.getch()

    def get_gpa(self,student_list:Student, stdscr):
        curses.endwin()
        score = []
        ect = []
        id = input("Enter the id of the student: ")
        if str(id) not in student_list.total or not id.isdigit():
            print("Invalid code or student's id is not in the list!")
        else:
            for i in self.total:
                if len(self.total[i]) == 2:
                    continue
                else:
                    ect.append(int(self.total[i][1]))
                    score.append(int(self.total[i][2][id]))
            if len(score) == 0 and len(ect) == 0:
                stdscr.addstr("Student does not have any grade!")
            else:
                stdscr.clear()
                stdscr.addstr("The GPA of the student is: " + str(math.floor(numpy.average(score, weights=ect)*10)/10))
            stdscr.refresh()
            stdscr.getch()
    

def main(stdscr):
    check = True
    while check:
        stdscr.clear()
        stdscr.addstr("""\nWhat operations do you want?
              1.Enroll a student
              2.Enter a new course
              3.Fill in students' grade
              4.Print students' list
              5.Print students' grade in one course
              6.Get a student's GPA
              7. Quit\n
              
              Enter your choice here: """)
        options = stdscr.getch()
        if options == ord("1"):
            student_list = Student(stdscr)
        elif options == ord("2"):
            course_list = Course(stdscr)
        elif options == ord("3"):
            course_list.enter_grade(student_list, stdscr)
        elif options == ord("4"):
            student_list.get_list(stdscr)
        elif options == ord("5"):
            course_list.get_grade(student_list, stdscr)
        elif options == ord("6"):
            course_list.get_gpa(student_list, stdscr)
        elif options == ord("7"):
            check = False
        else:
            print("Invalid code. Please enter again.")

wrapper(main)
        