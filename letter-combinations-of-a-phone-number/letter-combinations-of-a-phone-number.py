class Solution(object):
    def letterCombinations(self, digits):
       
        if digits == '': 
            return []
        temp = { '2': 'abc','3': 'def','4': 'ghi','5': 'jkl','6': 'mno',
                     '7': 'pqrs','8': 'tuv','9': 'wxyz',}
        chars = []
        
        for d in digits:
            chars.append(temp[d])
        l = list(itertools.product(*chars))
        ans = []
        for i in l:
            ans.append(''.join(i))
            
        return ans