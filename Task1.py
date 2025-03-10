student_marks = {
    "Adarsh": 99,
    "Sudhanshu": 98,
    "Amit": 92,
    "Raj": 88,
    "Ayush": 95
}

student_name = input("Please enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found. Please check the name and try again.")