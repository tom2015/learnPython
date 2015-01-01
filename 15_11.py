from IPython import embed
import random


def find_num(L):
    x = len(L)
    for i in range(1,x):
        if L[i] < L[i-1]:
            for j in range(i,-1,-1):
                tmp = L[j]
                L[j] = L[j-1]
                L[j-1] = tmp        
        else:
            continue       
    print L       






def insert_sort(L):
    N = len(L)
    for i in range(1,N):
        val = L[i]
        for j in range(i,-1,-1):
            if val>=L[j-1]: break
            L[j] = L[j-1]
        L[j]=val                        # val always insert at [j]





L = [9,4,8,2,1,10,0]

for _ in xrange(10):
    random.shuffle(L)
    print L ,
    insert_sort2(L)
    print '==> %s'%L
#find_num(L)
