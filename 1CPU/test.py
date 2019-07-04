def Fibonacci(n): 
    if n < 0: 
        print("Incorrect input")
        return
    # First Fibonacci number is 0 
    if n == 1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2) 

n = 100
print('Calculating Fibonacci ' + str( n ))
f = Fibonacci( n )
print('Fibonacci ' + str( n ) + ' == ' + str( f ))

