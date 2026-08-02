'''5X10=50
   5X9=45
   .
   .
'''
n=int(input("Enter the number:"))

for i in range(1,11):
    print(f"{n} X {11-i} ={n*(11-i)}")
    #10 1=11
    #9 2=11    thats why the logic is (11-i)