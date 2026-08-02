class Employee:
    company="ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is{self.salary}")
class Programer(Employee):
    company="TCS"
    def show_language(self):
        print(f"The name is {self.name} and the salary is{self.language}")

a=Employee()
b=Programer()
print(a.company,b.company)

'''THis is anormal class function and basically inharitance is the edited 
    verson of the class function that help us to reduse the lines of clas 
    function......
NORMALE-
    class Programer:
    company="TCS"
    def show(self):
        print(f"The name is {self.name} and the salary is{self.salary}")   
    def show_language(self):
        print(f"The name is {self.name} and the salary is{self.language}")
INHARITANCE-
    class Programer(Employee):
    company="TCS"
    def show_language(self):
        print(f"The name is {self.name} and the salary is{self.language}")

'''