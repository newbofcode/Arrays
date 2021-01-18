# Arrays
This is the first lab that helps students relearn arrays
1. given an array whose size is an even number, and you are to switch the first and the second half.
2. rearranging all elements in an array so that the even numbers come first. Otherwise, the order doesn’t matter.
3. Determining the sequence of array sizes requires a manual inspection of the output of that program. Redesign the experiment so that the program outputs only those values of k at which the existing capacity is exhausted.
4. Our DynamicArray class, as given in Code Fragment 5.3, does not support use of negative indices with get item . Update that method to better match the semantics of a Python list.
5. In the case when a resize occurs, the resize operation takes time to copy all the elements from an old array to a new array, and then the subsequent loop in the body of insert shifts many of those elements. Give an improved implementation of the insert method, so that, in the case of a resize, the elements are shifted into their final position during that operation, thereby avoiding the subsequent shifting.
