a = []
b = int(input("Enter the number of students: "))  # Store the number, don't print here
for i in range(b):
    c = int(input("Enter the marks: "))  # Store marks directly
    a.append(c)

print("Original list:", a)
a.sort()
print("Sorted list:", a)
