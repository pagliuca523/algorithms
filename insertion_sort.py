#Algo insertion sorting, purpose of studying, can be updated later.
import time
from random import randint

def insertionSort(alist):
    start_time = time.time()
    for j in range(1, len(alist)):
        key = alist[j]
        #// Insert alist[j] into the sorted sequence
        i = j
        while (i > 0) and (alist[i-1] > key):
            alist[i] = alist[i-1]
            i= i-1
        alist[i] = key
    print (time.time() - start_time)
if __name__ == '__main__':        
    #alist = [5,2,4,6,1,3]
    #Creating a randomic array
    ARRAY_LENGTH = 100
    alist = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    insertionSort(alist)
    print(alist)
    
