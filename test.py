#Bubble-----------------------------------------------
def sort_1(L):
     x = len(L)
     for i in range(x-1):
         for j in range(1,x-i):
             if L[j-1] <= L[j]: continue
             tmp = L[j-1]
             L[j-1] = L[j]
             L[j] = tmp
     print L 

#Insert-----------------------------------------------
def sort_2(L):
    for i in range(1,len(L)):
        val = L[i]
        for j in range(i,-1,-1):
            if val >= L[j-1]: break             
            L[j] = L[j-1]
        L[j] = val
    print L

#slect------------------------------------------------
def find_min(s,e):
    val,idx = L[s],s
    for i in range(s,e-1):
        if val <= L[i+1]: continue
        val = L[i+1]
        idx = i+1
    return idx

def sort_3(L):
    x = len(L)
    for j in range(x):
        id_ = find_min(j,x)        
        tmp = L[j]
        L[j] = L[id_]
        L[id_] = tmp
    print L

#-----------------------------------------------------
L = [1]
sort_3(L)
