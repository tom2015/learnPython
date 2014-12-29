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

def print_line_3(num):
    line0 = [0,1]
    line1 = [0,]
    for i in range(1,num+1):
        for j in range(1,i+1):
            val = line0[j-1] + line0[j]
            print val,
            line1.append(val)
        print '\n'
        line1.append(0)
        line0 = line1
        line1 = [0,]

print_line_3(1)


def pascals_triangle(n):
    x=[[1]]
    for i in range(n-1):
        x.append([sum(i) for i in zip([0]+x[-1],x[-1]+[0])])
    return x


for x in pascals_triangle(5):
        print('{0:^16}'.format(x))

