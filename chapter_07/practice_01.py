'''
    *
   ***
  *****
 *******
*********
(n=5)
'''
n=int(input("Enter the sserise of number:"))

for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))