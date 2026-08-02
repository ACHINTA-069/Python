with open("replace.txt") as f:
    lines=f.readlines()

line_no=1
for line in lines:
    if("Donkey" in line):
        print(f"yes are is preasent in line no:{line_no}")
        break
    line_no+=1
else:
        print("no are is not preasent ")