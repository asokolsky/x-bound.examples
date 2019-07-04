from multiprocessing import Pool

def Fibonacci( n ): 
    if n < 0: 
        print("Incorrect input")
        return 0
    # First Fibonacci number is 0 
    if n == 1: 
        return 0
    # Second Fibonacci number is 1 
    if n == 2: 
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2) 

cpus = 3
n = 100
print('Calculating Fibonacci ' + str( n ) + ' using ' + str(cpus) + 'CPUs')
p = Pool( cpus )
args = [n]*10
f = p.map(Fibonacci, [n]*cpus)
print('Fibonacci ' + str( n ) + ' == ' + str( f ) + ' * ' + str(cpus))

