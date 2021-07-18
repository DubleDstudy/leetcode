class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(0,n+1):
            tt=0
            temp=bin(i)
            temp=temp[2:]
            tt=temp.count('1')
            ans.append(tt)
        return ans
            