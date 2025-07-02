class Solution:
    def myAtoi(self, s: str) -> int:
        result = []
        sign = []
        for c in s:
            if c.isdigit():
                result.append(c)
            elif c == ' ':
                if len(result) == 0 and len(sign) == 0:
                    continue
                else: break
            elif (c == '+' or c == '-') and len(result) == 0 and len(sign) == 0:
                if c == '-': sign.append(-1)
                else: sign.append(1)
                continue
            else: break
        
        if (len(result) == 0): return 0

        num = int("".join(result))
        if (len(sign) > 0): num *= sign[0]
        max = 2**31 - 1
        min = -1*2**31
        if num > max: return max
        elif num < min: return min
        else: return num 


    
test_1 = Solution().myAtoi("42")
print(f"test_1 = {test_1} | Expected = 42")

test_2 = Solution().myAtoi( "+-012")
print(f"test_2 = {test_2} | Expected = -12")