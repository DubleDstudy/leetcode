class Solution:
    def decodeString(self, s: str) -> str:
        times_stack = []
        str_stack = []
        temp_str = ""
        times = ""
        for char in s:
            # check if number
            if ord(char) >= ord('0') and ord(char) <= ord('9'):
                times = times + char
            elif char == "[":
                times_stack.append(int(times))
                str_stack.append(temp_str)
                temp_str = ""
                times = ""
            elif char == "]":
                temp_str = times_stack.pop() * temp_str
                temp_str = str_stack.pop() + temp_str
            else:
                temp_str = temp_str + char
        return temp_str