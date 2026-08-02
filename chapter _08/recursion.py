def fac(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fac(n-1)
n=int(input("Enter the number:"))
print(f"The Factorial of the number {n} is:{fac(n)}")    