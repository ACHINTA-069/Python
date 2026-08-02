words=["Donkey","Bad","Boy","Harry"]

with open("replace.txt","r") as f:
    content=f.read()
for word in words:
    newContent=content.replace(word,"#" * len(word))

with open("replace.txt","w") as f:
    f.write(newContent)