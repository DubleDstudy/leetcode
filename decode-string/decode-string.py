class Solution:
    def decodeString(self, s: str) -> str:
        int_stack = []
        str_stack = []
        ans = ""
        times = ""
        for temp in s:
            # check if number
            if temp.isdigit():
                times = times + temp
            elif temp == "[":
                int_stack.append(int(times))
                str_stack.append(ans)
                ans = ""
                times = ""
            elif temp == "]":
                ans = int_stack.pop() * ans
                ans = str_stack.pop() + ans
            else:
                ans = ans + temp
        return ans
