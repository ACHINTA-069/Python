class Calculater:
    def __init__(self,n):
        self.n=n
    def square(self):
            print(f"The square is:{self.n*self.n}")
    def quabe(self):
         print(f"The quabe is:{self.n*self.n*self.n}")    
    def squareroot(self):
         print(f"The square-root is:{self.n**1/2}")

a=Calculater(4)
a.square()
a.quabe()
a.squareroot()        