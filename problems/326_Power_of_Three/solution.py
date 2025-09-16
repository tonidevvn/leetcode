class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True

        while True:
            if n / 3 == 1 and n % 3 == 0:
                return True
            elif n % 3 != 0:
                return False
            else:
                n /= 3
