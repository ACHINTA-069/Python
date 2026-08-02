class Employee:
    language="Python"
    salary=1200000


harry=Employee()
harry.name="Harry"  # Instance attridute(this is the higher priority attriduite)......
print(harry.language,harry.salary,harry.name)

rohan=Employee()
rohan.name="Rohan"
print(rohan.salary,rohan.language,rohan.name)
# Here "name" is "object" attribute and "salary" , "language" are "class" attribute because they- 
# -are directly belong to the class.......