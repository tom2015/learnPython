from IPython import embed

def merge_list(A,B):
    szA = len(A)
    szB = len(B)

    iA,iB = 0, 0
    rs = []

    while iA<szA and iB<szB:
        if A[iA]>B[iB]:
            rs.append(B[iB])
            iB =iB + 1
        else:
            rs.append(A[iA])
            iA = iA +1
    #--
    rs.extend(A[iA:])
    rs.extend(B[iB:])
    return rs




def merge_sort(L):
    sz = len(L)
    if sz<2 : return L

    mid = sz/2
    A = merge_sort(L[:mid])
    B = merge_sort(L[mid:])
    
    return merge_list(A,B)


if __name__=='__main__':
    import random

    if 0:
        A = [1,]
        B = [2,]

        L = merge_list(A,B)
        #assert L==[1,2,3,4,5,]
        print L


    L = range(5)
    random.shuffle(L)

    print L , '==>' ,

    rs = merge_sort(L)
    assert rs==range(5)

    print rs








