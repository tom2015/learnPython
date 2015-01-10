import random
from IPython import embed

'''
def quick_sort(L):
    i = 0
    j = (len(L))-1
    val = L[0]
    while i < j and j > i:
        while True:
            print '9:  L[j]<val,  %s|%s, j|%s'%(L[j],val,j)
            if L[j] < val:
                L[i] = L[j]
                print '12  L|%s'%L
                break
            else:
                j = j-1
                print '16  i|%s j|%s'%(i,j)
                if j == i:
                    break
                continue
        print i,j,L
        while True:
            if L[i] > val:
                L[j] = L[i]
                break
            else:
                i = i+1
                if i == j:
                    break
                continue
        #print L,i,j
        #embed()
    L[i] = val
    print L

'''



def quick_sort(L):
    if not L:   return L

    i,j = 0,len(L)-1
    val = L[0]


    while i!=j:
        while L[j]>=val and i!=j:  j = j-1        
        if i==j:  break
        
        L[i] = L[j]
        i = i+1
        
        while L[i]<=val and i!=j:  i = i+1
        if i==j:  break
        
        L[j] = L[i]
        j = j-1

    pre_half = quick_sort(L[:i])
    post_half = quick_sort(L[i+1:])
    
    return pre_half + [val,] + post_half



if __name__=='__main__':
    
    N = 15
    L = range(N)
    random.shuffle(L)
    #print L
    
    rs = quick_sort(L)
    #print rs
    assert rs==range(N)

    assert [] == quick_sort([])
    assert [1,] == quick_sort([1,])
    assert [1,1] == quick_sort([1,1])
    assert [1,1,2] == quick_sort([1,2,1])

