#!/usr/bin/env python3
#
# launch it like this:
# $ python3 ./test.py 10
# or
# $ python3 ./test.py
# 
# Default Fibonacci number to calculate - overwrite it on a command line:
# $ python3 ./test.py 10
n = 60
#
# nothing to customize below..
#
import sys
import time
import datetime

def Fibonacci( n ): 
    if n < 0: 
        print("Incorrect input")
        return
    # First Fibonacci number is 0 
    if n == 1: 
        return 0
    # Second Fibonacci number is 1 
    if n == 2: 
        return 1
    return Fibonacci( n-1 ) + Fibonacci( n-2 ) 

def FibonacciVerbose( n ):
    print( 'Fibonacci(', n, ') => ', end='', flush=True )
    pt1 = time.process_time()
    #pc1 = time.perf_counter()    
    f = Fibonacci( n )
    #pc2 = time.perf_counter()
    pt2 = time.process_time()
    dt = round( pt2 - pt1, 2 )
    print( f, 'in', datetime.timedelta(seconds=dt) )
    return


if __name__ == '__main__':
    try:
        n = int( sys.argv[-1] )
    except:
        pass

    try:
        for i in range(2, n+1):
            FibonacciVerbose( i )
    except KeyboardInterrupt:
        #print( '\nProcess KeyboardInterrupt' )
        pass
    except Exception as e:
        print( '\nProcess caught:', str( e ) )
    finally:
        print( '' )
        pass
