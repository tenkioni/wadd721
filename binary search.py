import sys

def binarysearch(seq,k):
        found = False

        while not found and len(seq) != 0: 
            middle = len(seq)//2
            if seq[middle] == k:
                found = True
            elif k < seq[middle]:
                seq = seq[:middle]
            else:
                seq = seq[middle+1:]
        return found

def main(): 
    errflg = 0
    sequence = [ i for i in range(0,100,3) ] 
    testing = [ (96,True), (33,True), (0,True), (99,True), (48,True), 
                (1, False), (31,False), (76,False), (98,False)] 

    for value, expected in testing: 
        result = binarysearch( sequence, value ) 

        print( "%s search for %d test, got %r expected %r" % \
                ("Passed" if result is expected else "Failed", value, result, expected) )

        if result is not expected: 
            errflg += 1

    return errflg

if __name__ == '__main__': 
    sys.exit( main() ) 
