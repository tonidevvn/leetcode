class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        placed = 0
        fIndex = 0
        for f in fruits:
            for bi in range(len(baskets)):
                if baskets[bi] >= f:
                    placed+= 1
                    baskets[bi] = -1
                    break
        
        return len(fruits) - placed
    