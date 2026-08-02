#with open("poem.txt","r") as f:
f=open("poem.txt")

content=f.read()
if("Twinkle" in content):
    print("Twinkle is in the content")
else:
   print("Twinkle is not in the content")    
f.close()   