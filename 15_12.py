from IPython import embed 
import random


L = [1,2,5,4,3,1,0]



'''
def find_min(s,e):  
    val,idx = L[s],s
    for i in range(s,e-1):
        if val <= L[i+1]: continue
        val = L[i+1]
        idx = i+1
    return idx



def sort_List():
    x = len(L)
    for j in range(x):
        id_ = find_min(j,x)        
        tmp = L[j]
        L[j] = L[id_]
        L[id_] = tmp

'''




def insert_sort(L):
    for i in range(1,len(L)):
        val = L[i]
        for j in range(i,-1,-1):
            if val >= L[j-1]: break         # find [j]            
            L[j] = L[j-1]
        L[j] = val
    #print L

for i in range(11):
    random.shuffle(L)
    print '%s: %s => '%(i,L) ,
    insert_sort(L)
    print L





        



                 