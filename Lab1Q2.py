#Yong Kang He
#500570639
#Lab 1 - Question 2
def q2(array1):
    arrayE = []
    arrayO = []
    for i in array1:
        if( i%2 == 0):
            arrayE.append(i)
        else:
            arrayO.append(i)
    print(arrayE + arrayO)
q2([1,4, 14, 2, 1, 3, 5, 6, 23])