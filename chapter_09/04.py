word="Donkey"

with open("replace.txt","r") as f:
    content=f.read()

newContent=content.replace(word,"######")

with open("replace.txt","w") as f:
    f.write(newContent)