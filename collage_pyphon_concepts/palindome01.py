def is_palindome(n):
    return str(n)==str(n)[::-1]
num=input("Enter the number to be checked:")
if is_palindome(num):
    print(f"The {num} is palindome")
else:
    print(f"The {num} is not palindome")

