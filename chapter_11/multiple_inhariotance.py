class Employee:
    company="ITC"
    name="Achinta Dey"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")
class Programer():
    language="Python"
    def print_language(self):
        print(f"The language is {self.language}")
class coder(Employee,Programer):
    company="TCS"
    def show_language(self):
        print(f"The company name is {self.company} and language is {self.language}")

a=coder()
a.show()
a.print_language()
a.show_language()