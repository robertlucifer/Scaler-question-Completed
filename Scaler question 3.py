#Given an array of integer A, find and return the minimum elements to be removed such that in the resulting array the sum of any two adject values is even number

# Input Format
# The only argument given is the integer array A.
# Output Format
# Return the minimum number of elements to be removed.

#for Example:
#Input 1:
# A = [1, 2, 3, 4, 5]
#Output 1:
# 1
#input 2:
# A = [2, 3, 4, 5, 6]
#Output 2:
# 1

#code
def solve(A):
    count=0
    for i in range(len(A)):
        if A[i]%2:
            count+=1
    return min(count, len(A)-count)


A = [1, 2, 3, 4, 5]
print(solve(A))