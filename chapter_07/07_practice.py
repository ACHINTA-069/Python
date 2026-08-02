'''
  *
 ***
*****(n=3)
'''
n=int(input("Enter the number of serise:"))

for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))