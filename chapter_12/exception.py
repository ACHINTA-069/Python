try:
    a=int(input("Hay,Enter a number:"))
    print(a)
except ValueError as v:
    print("Hey")
    print(v)

except Exception as e:
    print(e)

print("Thank You.....")