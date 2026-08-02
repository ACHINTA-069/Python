with open("myfile.txt") as f:
    content=f.read()
if("Achinta" in content):
    print("Achinta is preasnt.....")
else:
    print("Achinta is not preasnt.....")