class Employee:
    a=1
class Programer(Employee):
    b=2
class Manager(Programer):
    c=3

o=Employee()
print(o.a) #"o.b" and "o.c" cant print here....

o=Programer()
print(o.a,o.b) #"o.c" cant print here.......

o=Manager()
print(o.a,o.b,o.c) # we can print "o.a","o.b","o.c" here..... 