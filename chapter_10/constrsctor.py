class Employee:
    language="Python"
    salary=1200000

    def __init__(self,name,salary,language): #__init__ is a dunder methode which is automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("I am automatic")


    def getInfo(self):
        print(f"The language is{self.language}.The salary is {self.salary}")
    def greet(self):
        print("|Good Morning|")    

harry=Employee("Achinta",1300000,"JavaScript")
# harry.name="Harry"
print(harry.name,harry.salary,harry.language)
