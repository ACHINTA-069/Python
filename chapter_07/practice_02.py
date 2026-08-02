'''
*****
 ***
  *(n=3)
'''
n=int(input("Enter the sserise of number:"))

for i in range(n):
    print(" "*i+"*"*(2*(n-i)-1))
    
for i in range(1,n+1):
     print(" "*(n-i)+"*"*(2*i-1))    
