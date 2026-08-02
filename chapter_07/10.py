'''
*****
 ***
  *
'''
n=int(input("Enter the serise of number:"))

for i in range(n):
    print(" "*i+"*"*(2*(n-i)-1))
