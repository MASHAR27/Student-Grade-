from Student import Student
print("Student Grade Manager")

print()
print()
print()

students = []
num_of_students = int(input("How many many students information you want to enter : "))
print()
for i in range(num_of_students):
    print(f"Enter the information for the student# {i+1} ")
    st_name = input("Enter the student's name: ").strip()
    st_id =   input("Enter the student's ID: ").strip()
    st_gr = int(input("Enter the student's grade: "))
    students.append(Student(st_name,st_id,st_gr))
    
    
print()    
print("Results:")
total_grade = 0
for st in students:
    st.details()
    print(f"Passed:  {st.has_passed()}")
    total_grade += st.grade
    
    

print(f"Average of the entire class is : {total_grade/len(students)} ")    
  
    
    