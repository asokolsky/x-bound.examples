import os

test_folder = 'd:\\temp\\'
test_repeats = 5

kbytes = 1024
mbytes = 1024 * kbytes
gbytes = 1024 * mbytes
test_file_size = 2 * gbytes

try:
    O_BINARY = os.O_BINARY
except:
    O_BINARY = 0
READ_FLAGS = os.O_RDONLY | O_BINARY
WRITE_FLAGS = os.O_WRONLY | os.O_CREAT | os.O_TRUNC | O_BINARY
BUFFER_SIZE = 1024 * 1024

def create_file( fname, fsize ) : 
    chunk = bytearray( test_file_size )
    try:
        f = os.open( fname, WRITE_FLAGS )
        os.write( f, chunk )
    finally:
        try:
            os.close(f)
        except:
            pass
    return

def copy_file( srcfname, dstfname ) :
    try:
        fsrc = os.open( srcfname, READ_FLAGS )
        stat = os.fstat( fsrc )
        fdst = os.open( dstfname, WRITE_FLAGS, stat.st_mode )
        while True:
            r = os.read(fsrc, BUFFER_SIZE)
            if not r:
                break
            os.write(fdst, r)
    finally:
        try:
            os.close(fsrc)
        except:
            pass
        try:
            os.close(fdst)
        except:
            pass
    return

if __name__ == '__main__':
    fn1 = test_folder + 'test.me'
    fn2 = test_folder + 'test-copy.me'
    try:
        for x in range(0, test_repeats):
            print( 'Writing...' )
            create_file( fn1, test_file_size )
            print( 'Reading & writing...' )
            copy_file( fn1, fn2 )
            #print( 'Done!' )
            os.remove( fn2 )
            os.remove( fn1 )

    except KeyboardInterrupt:
        print( 'Main KeyboardInterrupt' )
    finally:
        try:
            print( 'Removing ' + fn1 )
            os.remove( fn1 )
        except:
            pass
        try:
            print( 'Removing ' + fn2 )
            os.remove( fn2 )
        except:
            pass
    pass
