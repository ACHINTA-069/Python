# If wwe dont want to apply self methode.Then we have to introduace_
# Static methode.The way to apply it is nothing but to add one line_
#before def and it is:@staticmethod.......
# Ex-     @staticmethod
#         def Hello()
#             print("Hello......")

class programer:
    company="Mycrosoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
p=programer("Achinta",1300000,722141)   
print(p.company)
print(p.name,p.salary,p.pin)
r=programer("Sayan",1000000,822141)   
print(p.company)
print(r.name,r.salary,r.pin)