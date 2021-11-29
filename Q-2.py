class Student:
    student_id=1
    student_name="AAKASH"
Student.student_class="COMP-B"
print(Student.__dict__)
del Student.student_name
print("\n Deleted student_name:\n")
print(Student.__dict__)