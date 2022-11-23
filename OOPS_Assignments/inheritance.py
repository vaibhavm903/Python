class Student:
    def __init__(self, name, roll_no, subject):
        self.name = name
        self.__rollNo = roll_no
        self._subject = subject

    def get_subject(self):
        return self._subject

    def set_subject(self, sub):
        self._subject = sub

    def get_rollno(self):
        return self.__rollNo

    def set_rollno(self, roll):
        self.__rollNo = roll

    def display_student_details(self):
        return f"\nName: {self.name}\nRoll Number: {self.__rollNo}\nSubject: {self._subject}"

    def __gt__(self, other_oj):
        return self.__rollNo > other_oj.__rollNo


class DBDA_student(Student):
    def __init__(self, name, roll_no, subject, primary_skill, sec_skills):
        super().__init__(name, roll_no, subject)
        self.primary_skill = primary_skill
        self.sec_skills = sec_skills

    def display_student_details(self):
        return super().display_student_details() + f"\nPrimary Skill: {self.primary_skill}\nSecondary Skills: {self.sec_skills}"

    def set_primary_skill(self):
        self.primary_skill = "SQL"


def main():
    student1 = DBDA_student("Vedant", 12, "Data Visualization", "Python", ["Tableau", "R", "Java"])
    student2 = DBDA_student("Hrishikesh", 15, "OOPS", "Java", ["Python", "Tableau", "Linux"])

    print("\nStudent Details======================================")
    print(student1.display_student_details())
    print(student2.display_student_details())

    print("\nDisplay Subject=======================")
    print(student1.get_subject())
    print(student2.get_subject())

    print("\nDisplay Roll Numbers================")
    print(student1.get_rollno())
    print(student2.get_rollno())

    student1.set_subject("Advance Analytics")
    student2.set_subject("Machine Learning")

    print("\nDisplay New Subject=======================")
    print(student1.get_subject())
    print(student2.get_subject())

    student1.set_primary_skill()
    print("Display Primary Skills====================")
    print(student1.primary_skill)
    print(student2.primary_skill)

    if student2 > student1:
        print("\nIf clause successful")
    else:
        print("\nElse clause successful")


if __name__ == "__main__":
    main()
