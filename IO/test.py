from datetime import datetime
from multiprocessing import Pool
import os
import sys
from typing import List

# test folder should have a trailing (back) slash for Windows
# test_folder = 'd:\\temp\\'

# for RPi4 - it seems dangerous to play with the boot SSD!  but...
#test_folder = '/boot/'
# this one is on SSD
test_folder = '/home/alex/'

# this many workers
cpus = 2
# each worker will repat test this may times
test_repeats = 2

kbytes = 1024
mbytes = 1024 * kbytes
gbytes = 1024 * mbytes
test_file_size = 1 * gbytes
#test_file_size = 101 * mbytes
# Perform file io using buffer this big
BUFFER_SIZE = 100 * mbytes

#
# nothing to customize below...
#
try:
    O_BINARY = os.O_BINARY
except:
    O_BINARY = 0
READ_FLAGS = os.O_RDONLY | O_BINARY
WRITE_FLAGS = os.O_WRONLY | os.O_CREAT | os.O_TRUNC | O_BINARY

def create_file( fname: str, fsize: int ) -> None:
    '''
    Create fsize big file named fname and init it with random data.
    '''
    print( f'Creating {fname} {fsize/mbytes} MBytes in size...' )
    t0 = datetime.now()
    #chunk = bytearray( fsize )
    chunk = os.urandom( fsize )

    try:
        f = os.open( fname, WRITE_FLAGS )
        os.write( f, chunk )

    finally:
        try:
            os.close(f)
        except:
            pass

    dt = datetime.now() - t0
    mbytes_per_sec = fsize / ( mbytes * dt.total_seconds() )
    print( f'Wrote {fname} @ { int(mbytes_per_sec) } MBytes/sec' )
    return

def copy_file( srcfname: str, dstfname: str ) -> None:
    '''
    Copy content of srcfname to dstfname.
    '''
    print( f'Copying {srcfname} to {dstfname}...' )
    bytesCopied = 0
    t0 = datetime.now()
    try:
        fsrc = os.open( srcfname, READ_FLAGS )
        stat = os.fstat( fsrc )
        fdst = os.open( dstfname, WRITE_FLAGS, stat.st_mode )
        while True:
            r = os.read(fsrc, BUFFER_SIZE)
            if not r:
                break
            os.write(fdst, r)
            bytesCopied += len( r )
    finally:
        try:
            os.close(fsrc)
        except:
            pass
        try:
            os.close(fdst)
        except:
            pass
    dt = datetime.now() - t0
    mbytes_per_sec = bytesCopied / ( mbytes * dt.total_seconds() )
    print( f'Copied {srcfname} to {dstfname} @ { int(mbytes_per_sec) } MBytes/sec' )
    return

def delete_files( *fnames: List[ str ] ) -> None:
    '''
    Delete files
    '''
    fns = ', '.join( fnames )
    print( f'Removing {fns}...' )
    for fname in fnames:
        try:
            os.remove( fname )
        except:
            pass
    return

def runner( i, test_repeats ):
    fn1 = None
    fn2 = None
    try:
        for x in range(0, test_repeats):
            fn1 = f'{test_folder}test{i}.me'
            fn2 = f'{test_folder}test{i}-copy.me'
            create_file( fn1, test_file_size )
            copy_file( fn1, fn2 )
            delete_files( fn1, fn2 )
            fn1 = None
            fn2 = None
        return 0

    except KeyboardInterrupt:
        print( f'Runner {i} KeyboardInterrupt' )

    finally:
        if fn1 is not None:
            delete_files( fn1, fn2 )

    return 1

if __name__ == '__main__':
    print( f'Generating IO using {cpus} proceses...' )
    p = Pool( cpus )
    t0 = datetime.now()
    try:
        args = [ (i, test_repeats) for i in range(cpus) ]
        f = p.starmap( runner, args )
        p.close()
        p.join()
        print( f'runner => {f}  * {cpus}' )

    except KeyboardInterrupt:
        print( 'Main KeyboardInterrupt' )

    except Exception as e:
        print( f'Main caught: {e}' )

    finally:
        dt = datetime.now() - t0
        print( f'done in { dt.total_seconds() } secs' )
