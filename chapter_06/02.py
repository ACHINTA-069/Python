sub1=int(input("enter the marsk of subject 1:"))
sub2=int(input("enter the marsk of subject 2:"))
sub3=int(input("enter the marsk of subject 3:"))

a=(((sub1+sub2+sub3)*100)/300)

if(sub1>33 and sub2>33 and sub3>33 and a>40):
    print("You are passed....",a)
else:
    print("You are fail.......",a)    