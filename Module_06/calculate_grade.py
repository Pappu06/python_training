class Student: # Define class

    def __init__(self, name, marks): # Self who refers to the current object
        self.name = name
        self.marks = marks

    def display_details(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        elif self.marks >= 60:
            return "C"

        else:
            return "D"


student1 = Student("Pappu", 85)

student1.display_details()

grade = student1.calculate_grade()

print("Grade:", grade)