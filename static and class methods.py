
class Employee:
    num = 0
    gross_income = 0

    def __init__(self,name,position,salary):
        self.name =name 
        self.position = position
        self.salary = salary
        Employee.num += 1
        Employee.gross_income += salary

    def post_info(self):                                            #Instance method
        print(f"{self.name} - {self.position}")
    
    @staticmethod
    def check_position(position):
        positions = ["Manager" , "Cook" , "Airbender" , "Monk"]      #For general purpose utiliy functions 
        return position in positions                                 #no need of class data

    @classmethod
    def no_of_employee(cls):                                           #For class-level data
        return f"No of employees : {cls.num}"                          #Used for variables in class itself

    @classmethod
    def gross_profit(cls):
        return f"The gross income of the company is {cls.gross_income}"


employee1 = Employee("Aang" , "Airbender",5200)
employee2 = Employee("Gyatsu", "Monk" , 10050)
employee3 = Employee("Appa" , "Manager", 50059)

employee1.post_info()
employee2.post_info()
employee3.post_info()

print(Employee.check_position("Firebender"))
print(Employee.no_of_employee())
print(Employee.gross_profit())


