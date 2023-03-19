from inputs import Input

def main():
    check = True
    while check:
        print("------------------------")
        options = input("""What operations do you want?
              1.Enroll a student
              2.Enter a new course
              3.Fill in students' grade
              4.Print students' list
              5.Print a student's grades
              6.Get a student's GPA
              7.Quit
              Enter it here: """)
        if options.isdigit():
            options = int(options)
            if options == 1:
                student_list = Input("student")
            elif options == 2:
                course_list = Input("course")
            elif options == 3:
                course_list.Enter_grade()
            elif options == 4:
                student_list.get_list_student(student_list)
            elif options == 5:
                course_list.get_grade(student_list, course_list)
            elif options == 6:
                student_list.get_gpa(student_list, course_list)
            elif options == 7:
                check = False
        else:
            print("Invalid code. Please enter again.")

if __name__ == "__main__":
    main()