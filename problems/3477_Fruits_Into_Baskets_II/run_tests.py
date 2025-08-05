from solution import Solution

def run_all_tests():
    sol = Solution()
    
    # Test 1: Basic test
    print("=== Test 1: Basic ===")
    fruits = [3, 5, 2]
    baskets = [2, 4, 6]
    result = sol.numOfUnplacedFruits(fruits, baskets)
    expected = 1
    print(f"Fruits: {fruits}, Baskets: {baskets}")
    print(f"Result: {result}, Expected: {expected}")
    print(f"Status: {'PASSED' if result == expected else 'FAILED'}")
    print()
    
    # Test 2: All unplaced
    print("=== Test 2: All unplaced ===")
    fruits = [1, 1, 1]
    baskets = [2, 2, 2]
    result = sol.numOfUnplacedFruits(fruits, baskets)
    expected = 3
    print(f"Fruits: {fruits}, Baskets: {baskets}")
    print(f"Result: {result}, Expected: {expected}")
    print(f"Status: {'PASSED' if result == expected else 'FAILED'}")
    print()
    
    # Test 3: All placed
    print("=== Test 3: All placed ===")
    fruits = [5, 6, 7]
    baskets = [1, 2, 3]
    result = sol.numOfUnplacedFruits(fruits, baskets)
    expected = 0
    print(f"Fruits: {fruits}, Baskets: {baskets}")
    print(f"Result: {result}, Expected: {expected}")
    print(f"Status: {'PASSED' if result == expected else 'FAILED'}")
    print()
    
    # Test 4: Empty fruits
    print("=== Test 4: Empty fruits ===")
    fruits = []
    baskets = [1, 2, 3]
    result = sol.numOfUnplacedFruits(fruits, baskets)
    expected = 0
    print(f"Fruits: {fruits}, Baskets: {baskets}")
    print(f"Result: {result}, Expected: {expected}")
    print(f"Status: {'PASSED' if result == expected else 'FAILED'}")
    print()
    
    # Test 5: Empty baskets
    print("=== Test 5: Empty baskets ===")
    fruits = [1, 2, 3]
    baskets = []
    result = sol.numOfUnplacedFruits(fruits, baskets)
    expected = 3
    print(f"Fruits: {fruits}, Baskets: {baskets}")
    print(f"Result: {result}, Expected: {expected}")
    print(f"Status: {'PASSED' if result == expected else 'FAILED'}")
    print()
    
    # Test 6: Duplicate baskets
    print("=== Test 6: Duplicate baskets ===")
    fruits = [2, 2, 2]
    baskets = [2, 2]
    result = sol.numOfUnplacedFruits(fruits, baskets)
    expected = 1
    print(f"Fruits: {fruits}, Baskets: {baskets}")
    print(f"Result: {result}, Expected: {expected}")
    print(f"Status: {'PASSED' if result == expected else 'FAILED'}")
    print()
if __name__ == "__main__":
    run_all_tests()
