class Student:

    class_year = "2023-2025"
    no_of_students = 0

    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.s = score
        Student.no_of_students += 1

    def intro(self):
        print(f"{self.name} is from Avatar The Last Airbender")

student1 = Student("Aang" , 112 , 97)
student2 = Student("Suko" , 15 , 100)
student3 = Student("Katara" , 13 ,93)
student4 = Student("Appa" , 117 , 25)

student3.intro()

print(student3.s)
print(f"No of students in the year {Student.class_year} is {Student.no_of_students}")

