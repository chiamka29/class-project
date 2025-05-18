grade_value = {"A": 5, "B": 4, "C": 3, "D": 2, "F": 0} 
total_grade = 0
actual_grade = 0
i = 0
course_units = []
while i < 6: 
    i += 1
    course = input("Enter the name of course " + str(i) + ": ")
    grade = input("What is your grade for " + course + ": ")
    while grade.upper() not in grade_value.keys(): 
        print("\nInvalid grade.")
        grade = input("What is our grade for " + course + ": ")
    units = input("How many units does " + course + " carry: ")
    while units not in "12346": 
        print("\nInvalid course units.")
        units = input("How many units does " + course + " carry: ")
    course_units += units
    total_grade += int(units)
    actual_grade += grade_value[grade.upper()] * int(units)
print("Your GPA is " + str(actual_grade/total_grade) + ".") 