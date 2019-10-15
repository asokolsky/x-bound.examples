#!/usr/bin/env python3
#
# launch it like this:
# $ python3 ./test.py 10 2
# or
# $ python3 ./test.py
# 
# Default Fibonacci number to calculate - overwrite it on a command line:
# $ python3 ./test.py 10 2
n = 50
# number of CPUs to use in parallel - overwrite it on a command line:
# $ python3 ./test.py 10 2
cpus = 3
#
# nothing to customize below..
#
import sys
import os
import time
import datetime
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

def FibonacciVerbose( n ):
    pt1 = time.process_time()
    #pc1 = time.perf_counter()    
    f = Fibonacci( n )
    #pc2 = time.perf_counter()
    pt2 = time.process_time()
    dt = round( pt2 - pt1, 2 )
    print( os.getpid(), 'Fibonacci(', n, ') => ', f, 'in', datetime.timedelta(seconds=dt) )
    return f

def FibonacciWrap( n ):
    try:
        for i in range(2, n+1):
            FibonacciVerbose( i )
        return 0
    except KeyboardInterrupt:
        #print( 'Worker KeyboardInterrupt' )
        pass
    except Exception as e:
        print( 'Worker caught:', str( e ) )
    finally:
        #print( 'Worker cleanup' )
        pass
    return 0

if __name__ == '__main__':
    try:
        n = int( sys.argv[-2] )
        cpus = int( sys.argv[-1] )
    except:
        pass

    print( 'Calculating Fibonacci', n, 'using', cpus, 'CPUs' )

    p = Pool( cpus )
    try:
        f = p.map( FibonacciWrap, [n] * cpus )
        p.close()
        p.join()
        print( 'Fibonacci', n, '=>', f )

    except KeyboardInterrupt:
        print( '' )
        pass
    except Exception as e:
        print( 'Main caught:', str( e ) )
    finally:
        #print( 'Main cleanup' )
        pass
