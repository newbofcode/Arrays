#Yong Kang He
#500570639
#Lab 1 - Question 3
import sys

def q3():
    data = []
    c=0
    for k in range(27):
        a = len(data)
        b = sys.getsizeof(data)
        if c==0 :
            c=b
        elif c!=b:
            print( "Length: {0:3d}; Size in bytes: {1:4d}" .format(a-1, c))
            c=b
        data.append(None)
q3()