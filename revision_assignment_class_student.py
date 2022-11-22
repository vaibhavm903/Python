# Create a Student class with following
#
# a) instance variables
#    Name,Rollno,Subject
# b) Instance Methods
#    get_subject
#    set_subject -- sets a subject for the particular instance

# c) Class variables
#    school_name
# d) Class methods
# 	get_school_name
# 	set_school_name -- sets a school name for the class
# e) static methods
# 	display_prerequiste_skills --> displays some skills for all students in general good to have ones
#
class Student:
    school_name = "CDAC"

    @classmethod
    def get_school_name(cls):
        return cls.school_name

    @classmethod
    def set_school_name(cls, new_name):
        cls.school_name = new_name

    def __init__(self, name, roll_no, subject):
        self.name = name
        self.roll_no = roll_no
        self.subject = subject

    def get_subject(self):
        return self.subject

    def set_subject(self, new_subject):
        self.subject = new_subject

    @staticmethod
    def display_prerequisite_skills():
        return "disciplined"

