class Student:
    total = {}
    total_count = 0
    
    def in_list(self,id):
        if id not in self.total:
            return False
        return True
    
    def __init__(self):
        print("\n")
        id = input("Enter student id: ")
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
    
    def get_list(self):
        for i in self.total:
            print("\n")
            print("Student id: " + i)
            print("Student name: " + self.get_name(i))
            print("Student date of birth: " + self.get_dob(i))
            print("\n")
    
class Course(Student):
    total = {}
    total_count = 0
    
    def in_list(self, id):
        if id in self.total:
            return True
        return False
    
    def __init__(self):
        print("\n")
        id = int(input("Enter a course's id: "))
        if self.in_list(id):
            print("ID already exist.")
        else:
            name = input("Enter the course's name: ")
            self.total[id] = [name]
    
    def get_name(self, id):
        return self.total[id][0]
    
    def enter_grade(self, student_list: Student):
        grade_list = []
        each = {}
        print("\n")
        id = input("Enter course ID that you want to enter grade: ")
        print("Course: " + self.get_name(int(id)))
        for i in student_list.total:
            print("\n")
            print("Student ID: " + i)
            print("Student name: " + student_list.get_name(str(i)))
            print("Student date of birth: " + student_list.get_dob(i))
            score = float(input("Enter the score of this student: "))
            each[i] = score
        grade_list = each
        self.total[int(id)].append(grade_list)
        
    def get_grade(self, student_list: Student):
        print("\n")
        id = int(input("Enter the course id that you want to show grade: "))
        if id not in self.total:
            print("ID not found")
        elif len(self.total[int(id)]) == 1:
            print("Grade is not updated!")
        else:
            print("Course: " + self.total[id][0])
            for i in self.total[int(id)][1]:
                print("-----------------")
                print("Student ID: " + str(i))
                print("Student's name: " + student_list.total[str(i)][0])
                print("Student's date of birth: " + student_list.total[str(i)][1])
                print("Grade: " + str(self.total[int(id)][1][i]))
    

def main():
    check = True
    while check:
        print("\n")
        print("""What operations do you want?
              1.Enroll a student
              2.Enter a new course
              3.Fill in students' grade
              4.Print students' list
              5.Print students' grade in one course
              6.Quit""")
        options = input()
        if options.isdigit():
            options = int(options)
            if options == 1:
                student_list = Student()
            elif options == 2:
                course_list = Course()
            elif options == 3:
                course_list.enter_grade(student_list)
            elif options == 4:
                student_list.get_list()
            elif options == 5:
                course_list.get_grade(student_list)
            elif options == 6:
                check = False
        else:
            print("Invalid code. Please enter again.")

if __name__ == "__main__":
    main()
        