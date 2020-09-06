
def Fibonacci( n: int ) -> int:
    '''
    Classical fibonacci algorithm
    '''
    if n < 0: 
        print( "Incorrect input" )
        return 0
    if n == 1: 
        return 0
    elif n==2: 
        return 1
    return Fibonacci( n-1 ) + Fibonacci( n-2 ) 

n = 40
print( f'Calculating Fibonacci {n}' )
f = Fibonacci( n )
print( f'Fibonacci {n} => {f}' )

