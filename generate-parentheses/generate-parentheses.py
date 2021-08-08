class Solution:
    def generateParenthesis(self, n):
        ans = []
        s = [("(", 1, 0)]
        while s:
            x, left, right = s.pop()
            if left - right < 0 or left > n or right > n:
                continue
            if left == n and right == n:
                ans.append(x)
            s.append((x+"(", left+1, right))
            s.append((x+")", left, right+1))
        return ans
        