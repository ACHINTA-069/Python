class Employee:
    language="Python"
    salary=1200000

    def getInfo(self):
        print(f"The language is{self.language}.The salary is {self.salary}")
    def greet(self):
        print("|Good Morning|")    

harry=Employee()
harry.language="JavaScript"    
harry.getInfo()
# Employee.getInfo(harry)
harry.greet()