class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
test_1 = Solution().strStr("sadbutsad", "sad")
print(f"test_1 = {test_1} | Expected = 0")

test_2 = Solution().strStr("leetcode", "leeto")
print(f"test_2 = {test_2} | Expected = -1")