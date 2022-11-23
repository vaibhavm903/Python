# ---------------------------------------
# Operator overloading Problems :
# ---------------------------------------
# Create a Student class with following 

# 	a) instance variables 
# 	   Name,Rollno,Subject
# 	b) Instance Methods
# 	   get_subject
# 	   set_subject -- sets a subject for the particular instance
	 
# 	Main Method:
# 		Create two student objectsfor ex: Student1,Student2
# 		display subject names for each of the above created objects
# 		set a new subject name for each of the above created objects 	
# 		display subject names again after updating for each of the above created objects
		
# 		compare Student1,Student2 for >,<,>=,<=,== in some if else block [Should have 5 methods for each operator ]
# 			if the condition evaluate to true print "If clause successful"
# 			if the condition evaluate to false print "Else clause successful"

class Student:

    def __init__(self, name, roll_no, subject):
        self.name = name
        self.roll_no = roll_no
        self.subject = subject

    def get_subject(self):
        return self.subject

    def set_subject(self, new_subject):
        self.subject = new_subject

    def __eq__(self, other):
        return self.roll_no == other.roll_no

    def __gt__(self, other):
        return self.roll_no > other.roll_no

    def __lt__(self, other):
        return self.roll_no < other.roll_no

    def __ge__(self, other):
        return self.roll_no >= other.roll_no

    def __le__(self, other):
        return self.roll_no <= other.roll_no


def main_method():
    s1 = Student(input("Enter Name"), int(input("Enter Roll No")), input("Enter Name"))
    print(s1.get_subject())
    s2 = Student(input("Enter Name"), int(input("Enter Roll No")), input("Enter Name"))
    print(s2.get_subject())
    s1.set_subject("Python")
    s2.set_subject("Hindi")
    print(s1.get_subject())
    print(s2.get_subject())
    if s1 == s2:
        print("If clause success")
    else:
        print("Else success ")

    if s1 > s2:
        print("If gt clause success")
    else:
        print("Else gt success ")

    if s1 < s2:
        print("If lt clause success")
    else:
        print("Else lt success ")

    if s1 >= s2:
        print("If ge clause success")
    else:
        print("Else ge"
              " success ")

    if s1 <= s2:
        print("If le clause success")
    else:
        print("Else le success ")


main_method()
