#Yong Kang He
#500570639
#Lab 1 - Question 5
def insert(self,k,value):
    if self._n == self._capacity:
        B= self._make_array(2*self._capacity)
        for j in range(self._n):
            if j < k:
                B[j] = self._A[j]
            else:
                B[j+1] = self._A[j]
    self._A =B
    self._A[k] = value
    self._capacity = 2*self._capacity
    self._n+=1