#Yong Kang He
#500570639
#Lab 1 - Question 4
def __getitem__(self,k):
    if k<0 and not (self._n*-1 <= k <0):
        raise IndexError('invalid index')
    if k > 0 and not 0<=k<=self._n:
        raise IndexError('invalid index')
    return self._A[k]