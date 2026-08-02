a=[]
b=int(input("Enter the no of student:"))
for i in range(b):
    c=int(input("entre the mask:"))
    a.append(c)

print("original list",a)
a.sort()
print("Sorted List",a)