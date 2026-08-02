def fibonacci_loop(n):
    a,b=0,1
    place=[]
    for _ in range(n):
        place.append(a)
        a,b=b,a+b
    return place 
temp=int(input("Enter thr no of terms:"))
fibonacci_series=fibonacci_loop(temp)
print(f"The Fibonacci Series upto{temp} terms is:{fibonacci_series}")

