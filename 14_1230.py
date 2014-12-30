from IPython import embed
from math import *




def find_num(num):
    #-- case: simplest:2
    if num==1:  return []

    #-- case: simpler 
    for i in range(2,num/2):
        if num%i!=0: continue               #<-- try next
        sub_result = find_num(num/i)        #<-- we get it, return result
        sub_result.append(i)
        return sub_result
    
    return [num,]                           #<-- num is prime number and greater than 1




def square(num):
    print '*'*num
    for i in range(2,num):
        print '*{0}*'.format(' '*(num-2))
    print '*'*num




def square(num):
    print (' '*(num-1)) + '*'
    for i in range(2,num):
        print (' '*(num-i)) +'*{0}*'.format(' '*(1+((i-2)*2)))
    print '*'*((num*2)-1)
   
   



        
        




if __name__=='__main__':

    if 0:
        num = 4090
        rs = find_num(num)

        #-- make sure 
        i = 1
        for e in rs:
            i = i * e

        assert(i==num)

        #-- output
        rs = [ '%s'%e for e in rs ]
        print '%s = %s'%(num, ' * '.join(rs))


    if 1:
        square(40)    




