import numpy as np
import math
class Output():
    def get_list_student(self, student_list):
        for i in student_list.s_list.total:
            if int(i) == 0:
                continue
            print("Student ID: " + str(i))
            print("Student name: " + str(student_list.s_list.total[int(i)]["name"]))
            print("Student date of birth: " + str(student_list.s_list.total[int(i)]["dob"]))
            print("___________")

    def get_grade(self, student_list, course_list):
        id = input("Enter the student ID that you want to get grade: ")
        if not student_list.s_list.in_list(int(id)):
            print("Student ID is not in the list.")
        else:
            grades = student_list.s_list.total[int(id)]["grade"]
            print(grades)
            print("Student ID: " + str(id))
            print("Student name: " + str(student_list.s_list.total[int(id)]["name"]))
            print("Student date of birth: " + str(student_list.s_list.total[int(id)]["dob"]))
            for i in grades:
                print("Subject: " + str(course_list.c_list.total[i]["name"]))
                print("Score: " + str(student_list.s_list.total[int(id)]["grade"][int(i)]))
                print("\n")

    def get_gpa(self, student_list, course_list):
        id = input("Enter the student ID that you want to get GPA: ")
        if not student_list.s_list.in_list(int(id)):
            print("Student ID is not in the list")
        else:
            if len(student_list.s_list.total[int(id)]["grade"]) == 0:
                print("There are no subjects for this student.")
            else:
                score = []
                ect = []
                for i in student_list.s_list.total[int(id)]["grade"]:
                    score.append(int(student_list.s_list.total[int(id)]["grade"][int(i)]))
                    ect.append(int(course_list.c_list.total[int(i)]["ect"]))
                print(score)
                print(ect)
                print("Student ID: " + str(id))
                print("Student name : " + str(student_list.s_list.total[int(id)]["name"]))
                print("Student date of birth: " + str(student_list.s_list.total[int(id)]["dob"]))
                print("GPA of student is: " + str((math.floor(np.average(score, weights=ect))*10)/10))

                  
