def get_student_number():
    return int(input("How many students are there in your class? "))

def get_student_info(student_number):
    info_per = []
    student_info = {}
    for i in range(student_number):
        info_per = []
        print("\n")
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth in format dd/mm/yyyy: ")
        info_per.append(name)
        info_per.append(dob)
        student_info[id] = info_per
    return student_info

def get_number_of_course():
    print("\n")
    return int(input("How many course they have? "))

def get_course_list(course_number):
    print("\n")
    course_list = {}
    for i in range(course_number):
        id = input("Enter id of the course: ")
        name = input("Enter name of the course: ")
        course_list[id] = name
    return course_list

def enter_grade(course_list, id, student_list):
    print("\n")
    subject_grade = {}
    temp = [[]]
    print("Subject " + course_list[str(id)] + ":")
    print("----------")
    for i  in student_list:
        print("Student's id: "+ i + ", name: " + student_list[i][0])
        grade_score = input("Grade? ")
        if temp == [[]]:
            temp = [[i, grade_score]]
        else:
            temp.append([i ,grade_score])
        print("\n")
    return temp

def print_student_list(student_list):
    print("Student list:\n")
    for i in student_list:
        print("Student id: " + i)
        print("Student's name: " + student_list[i][0])
        print("Student's date of birth: " + student_list[i][1])
        print("-----")
    print("\n\n")

def print_course_list(course_list):
    print("Course list: ")
    for i in course_list:
        print("Subject id: " + i)
        print("Subject name: " + course_list[i])
    print("\n\n")

def print_grade(i:str, control_grade, student_list, course_list):
    print("\n")
    print("Subject name: " + course_list[str(i)])
    print("-------------")
    for j in control_grade[i]:
        print("Student id: " + str(j[0]))
        print("Student's name: " + student_list[str(j[0])][0])
        print("Grade: " + str(j[1]))
        print("\n")
    print("\n\n")

def main():
    student_number = get_student_number()
    student_list = get_student_info(student_number)
    course_number = get_number_of_course()
    course_list = get_course_list(course_number)
    id = int(input("What course you want to enter students' grade? "))
    if str(id) not in course_list:
        while str(id) not in course_list:
            id = int(input("Enter the correct ID: "))
    control_grade = {}
    control_grade[id] = enter_grade(course_list, id, student_list)
    print_student_list(student_list)
    print_course_list(course_list)
    for i in control_grade:
        print_grade(i, control_grade, student_list, course_list)


if __name__ == "__main__":
    main()