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
            print x,
        print '\n'
    




print_line_2(10)

