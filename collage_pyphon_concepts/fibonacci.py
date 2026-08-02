def fibonacci_loop(n):
    a,b=0,1
    serise=[]
    for _ in range(n):
        serise.append(a)
        a,b=b,a+b
    return serise
terms=10
fib_sequence=fibonacci_loop(terms)
print(f"The Fibonacci serise up to {terms} terms:{fib_sequence}")
