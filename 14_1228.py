from IPython import embed

def print_line_1():
    for row in range(1,10):         # [1, 10)   =>   size = 9
        for x in range(1,row+1):    # [1,row+1) => size = row
            print x ,
        # new line
        print '\n'




def print_line_2(num):
    for row in range(1,num+1):
        for x in range(1,num+2-row):
            print x
            print '\n'
'''
def print_line_3(num):
    cursum = 0
    pre = [0,1]
    cur = [0,]
    for i in range(1,num+1):
        for j in range(1,i+1):
            val = pre[j-1] + pre[j]
            #print val,
            cur.append(val)
            cursum = cursum + val            
        print cursum
        vals = ['%s'%e for e in cur[1:]]
        vals = ','.join(vals)
        print '{0:^16}'.format(vals)
        cur.append(0)
        pre = cur
        cur = [0,]

print_line_3(6)
 

def pascals_triangle(n):
    x=[[1]]
    for i in range(n-1):
        x.append([sum(i) for i in zip([0]+x[-1],x[-1]+[0])])
    return x

'''
L = []


def gen_next(L):
    if not L: return [1,]
    mlist = [1,]    
    x = len(L)
    for j in range(1,x):
        val = L[j-1] + L[j]
        mlist.append(val)
    mlist.append(1)
    return mlist

def my_gen_next(L):
    mlist,Lj_1 = [], 0    
    for e in L:
        mlist.append(Lj_1 + e)
        Lj_1 = e
    mlist.append(1)
    return mlist



for i in range(5):
    L = gen_next(L)
    print L



#for x in pascals_triangle(5):
#        print('{0:^16}'.format(x))

