student_marks = {
    'Alice': 88,
    'Bob': 75,
    'Charlie': 92,
    'Diana': 67
}

name = input("Enter a student's name to find their marks: ")

marks = student_marks.get(name, "Student not found.")
print(f"Marks: {marks}")
