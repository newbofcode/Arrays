#Yong Kang He
#500570639
#Lab 1 - Question 1
def q1():
    array1 = [9,13,21,4,11,7,1,3]
    array2 = array1[4:] +array1[:4]
    sum1=0
    sum2 =0
    count=0
    for i in array2:
        if count < len(array2)/2:
            sum1+= i
            count+=1
        else:
            sum2 +=i
    print(array2)

    print("The average of the new first half is {}".format(sum1/count))

    print ("The average of the new second half is {}".format(sum2/count))
q1()