class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt=0
        def palindrom(S:str):
            return S==S[::-1]
        for i in range(len(s)):
            for j in range (1,len(s)-i+1):
                if palindrom(s[i:i+j]):
                    cnt+=1
        return cnt