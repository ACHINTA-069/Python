class Employee:
    def __init__(self):
        print("Constructor of Employee")
        

class Programmer(Employee):
    def __init__(self):
        super().__init__()    # calls Employee's __init__
        print("Constructor of Programmer")
  
class Manager(Programmer):
    def __init__(self):
        super().__init__()    # calls Programmer's __init__
        print("Constructor of Manager")
    
o = Manager()
