a=int(input("Enter the number:"))
if(a==1):
    print(f"The number({a}) is not prime.")   
elif(a==2):
    print(f"The number({a}) is prime.")      
else:
    for i in range(2,a):
        if(a%i)==0:
            print(f"The number({a}) is not prime.")    
            break
    else:
        print(f"The number({a}) is prime.")