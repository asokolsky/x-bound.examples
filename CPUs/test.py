#
#
#

# # of CPUs to use in parallel
cpus = 3
# Fibbonacci number to calculate
n = 50

# nothing to customize below..
from multiprocessing import Pool

cachedResult = []
for i in range(n + 1):
    cachedResult.append( 0 )
#print(len(cachedResult))

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

    global cachedResult
    res = cachedResult[ n ]
    if( res ):
        return res
    res = Fibonacci(n-1) + Fibonacci(n-2)
    #cachedResult[ n ] = res
    #print('Fibonacci', str( n ), '=>', str( res ))
    return res

def FibonacciWrap( n ):
    try:
        return Fibonacci( n )
    except KeyboardInterrupt:
        print( 'Process KeyboardInterrupt' )
    except Exception as e:
        print( 'Process caught:', str( e ) )
    finally:
        print( 'Process cleanup' )
    return 0

if __name__ == '__main__':
    print('Calculating Fibonacci', str( n ), 'using', str(cpus), ' CPUs')
    p = Pool( cpus )
    try:
        f = p.map( FibonacciWrap, [n] * cpus )
        p.close()
        p.join()
        print( 'Fibonacci', str( n ), '==', str( f ), ' * ', str( cpus ) )
    except KeyboardInterrupt:
        print( 'Main KeyboardInterrupt' )
    except Exception as e:
        print( 'Main caught:', str( e ) )
    finally:
        print( 'Main cleanup' )
