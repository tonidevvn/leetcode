class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n == 1: 
            return True
        
        def sort_digits(num):
            return "".join(sorted(str(num)))

        possible_numbers = []
        count = 0
        num = 0
        while True:
            num = 2 ** count
            if len(str(num)) == len(str(n)):
                possible_numbers.append(num)
            elif len(str(num)) > len(str(n)):
                break
            count += 1

        sorted_n = sort_digits(n)
        for num in possible_numbers:
            if sorted_n == sort_digits(num):
                return True

        return False