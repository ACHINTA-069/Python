a=int(input("Enter a:"))
b=int(input("Enter b:"))

if(a==0 or b==0):
    raise ZeroDivisionError("Our programe is not made todevide numbers by zero")
else:
    print(f"Devitin is:{a/b}")