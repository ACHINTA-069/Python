'''
1 for snake
-1 for water
0 for gun
'''
import random
computer=random.choice([-1,0,1])
your_choice=input("Enter your choice among 's'(snake),'w'(water),'g'(gun):").lower()
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",0:"gun",-1:"water"}

you=youDict[your_choice]

#Now we have two choices you and computer..........
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(you==computer):
    print("It's a Draw.....")
else:
    if(computer==1 and you==-1):
        print("Computer Win.....") 
    elif(computer==1 and you==0):
        print("You Win.....")
    elif(computer==0 and you==1):
        print("Computer Win.....")
    elif(computer==0 and you==-1):
        print("You Win.....")
    elif(computer==-1 and you==0):
        print("Computer Win.....")
    elif(computer==-1 and you==1):
        print("You Win.....")
    else:
        print("Somethin went wrong!")   
               