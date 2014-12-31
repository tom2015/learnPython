
n = 100



def find_prime(n):
    rs = []
    for p in range(1, n+1):
        found = True
        for i in range(2, p):
            if p % i != 0:  continue    # try next i, check p%i 
            found = False
            break
        
        if not found:   continue        # try next p
        rs.append(p)
    return rs

L = [1,10,9,8,7,6,5,4,3,2,1,0,90]
 
 
 


def find_max_num(L):
     x = len(L)
     for i in range(x-1):
         for y in range(1,x-i):
             if L[y-1] >= L[y]: continue
             tmp = L[y-1]
             L[y-1] = L[y]
             L[y] = tmp
     print L 


find_max_num(L)

'''
if __name__=='__main__':
    print find_prime(12340545)
'''

