f=open("file.txt","r") #open function containts two bites-
                       #-one for name of the file and mode of the file... 
data=f.read()          #"r"means-read of the file
print(data)
f.close()