class Solution:
    def numTrees(self, n: int) -> int:  
        temp=[0 for i in range(n+1)]
        temp[0]=1
        temp[1]=1

        for i in range(2,len(temp)):
            for j in range(i):
                temp[i] += temp[j] * temp[i-j-1]
        return temp[n]