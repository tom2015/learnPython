from IPython import embed



        


'''

a = []
b = [1,2,3,4]


mylist = []

if len(a) < len(b):
    x = len(a)
else:
    x = len(b)


i = 0
j = 0

while 1:
    if i == x: 
        mylist.extend(b[j:])
        break
    if j == x:
        mylist.extend(a[i:])
        break

    vala = a[i]
    valb = b[j]
    #print i,j,x,mylist
  
    if vala < valb:
        mylist.append(vala)
        i = i+1
    if vala > valb:
        mylist.append(valb)
        j = j+1
    if vala == valb:
        mylist.append(vala,valb)


print mylist
    
'''



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



if __name__=='__main__':


    A = [1,]
    B = [2,]

    L = merge_list(A,B)
    #assert L==[1,2,3,4,5,]
    print L









