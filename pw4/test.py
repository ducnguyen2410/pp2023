from input import Input

def main():
    student_list = {}
    course_list = {}
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
                student_list = Input("student")
            elif options == 2:
                course_list = Input("course")
            elif options == 3:
                course_list.Enter_grade()
            elif options == 4:
                student_list.get_list()
            elif options == 5:
                course_list.get_grade(student_list)
            elif options == 6:
                course_list.get_gpa(student_list)
            elif options == 7:
                check = False
        else:
            print("Invalid code. Please enter again.")

if __name__ == "__main__":
    main()