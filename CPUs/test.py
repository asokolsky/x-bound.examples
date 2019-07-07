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

def FibonacciWrap( n ):
    try:
        return Fibonacci( n )
    except KeyboardInterrupt:
        print( 'Process KeyboardInterrupt' )
    except Exception as e:
        print( 'Process caught: ' + str( e ) )
    finally:
        print( 'Process cleanup' )
    return 0

if __name__ == '__main__':
    cpus = 5
    n = 100
    print('Calculating Fibonacci ' + str( n ) + ' using ' + str(cpus) + ' CPUs')
    p = Pool( cpus )
    try:
        f = p.map( FibonacciWrap, [n] * cpus )
        p.close()
        p.join()
        print( 'Fibonacci ' + str( n ) + ' == ' + str( f ) + ' * ' + str( cpus ) )
    except KeyboardInterrupt:
        print( 'Main KeyboardInterrupt' )
    except Exception as e:
        print( 'Main caught: ' + str( e ) )
    finally:
        print( 'Main cleanup' )
