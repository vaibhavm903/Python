from revision_assignment_class_student import *

# Main Method:
# 	Create two student objects
student1 = Student("Tushar", "09", "Python")
student2 = Student("Vaibhav", "56", "Java")

# 	display subject names for each of the above created objects
print(student1.get_subject())
print(student2.get_subject())

# 	set a new subject name for each of the above created objects
print(student1.set_subject("Hadoop"))
print(student2.set_subject("Machine Learning"))

# 	display subject names again after updating for each of the above created objects
print(student1.get_subject())
print(student2.get_subject())

# 	display the class variable
print(Student.get_school_name())

# 	update the class variable using set_school_name method
Student.set_school_name("Sunbeam")

# 	display the class variable
print(Student.get_school_name())

# 	update the class variable using class_name. notation
Student.school_name = "Know IT"

# 	display the class variable
print(Student.get_school_name())

# 	update the class variable using object_name. notation
student1.school_name = "IIT"

# 	display the class variable
print(Student.get_school_name())

# 	display the object variable with the same name as class variable for the object you selected on line27
print(student1.school_name)

# 	delete the school_name instance variable for the object you selected on line27
del student1.school_name

# 	display the object variable with the same name as class variable for the object you selected on line27
print(student1.school_name)

# 	delete the the object you selected on line27
del student1

# 	display the rollno for the object you selected on line27
print(student1.roll_no)

# 	delete the school_name for the class
del Student.school_name

# 	display the class variable
print(Student.school_name)
