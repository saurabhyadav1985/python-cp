class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = set()
        size = len(nums)

        for i in range (size):
            if i not in visited:
                cycle_set = set()

                while True:
                    if i in cycle_set:
                        return True

                    visited.add(i)
                    cycle_set.add(i)

                    prev, i = i, (i + nums[i]) % size

                    #unicycle
                    if prev == i:
                        break
                    #sign difference
                    if nums[prev] > 0 != nums[i] < 0:
                        break 
                    

        return False
        
'''
This algorithm basically iterates over each index in the array, visiting each index once. It checks for cyclic patterns using a set to track visited indices in the current cycle. If a circular loop is detected, it returns True, otherwise False. 

The time complexity of the given algorithm is O(n^2), where n is the size of the input list nums. This is because the algorithm uses nested loops: the outer for loop iterates n times (where n is the size of nums), and the inner while loop can also iterate up to n times in the worst case.

The space complexity of the algorithm is O(n), where n is the size of nums. This is because the algorithm uses additional sets (visited and cycle_set) to store visited indices. The space required by these sets grows linearly with the size of nums.

Overall, the algorithm has a quadratic time complexity due to the nested loops, and a linear space complexity. Depending on the size of the input, it may not be the most efficient solution for large arrays.
'''

    def betterSolution(self, nums: List[int]) -> bool:
        def move(i):
            return (i + nums[i]) % len(nums)
            
        for i in range(len(nums)):
            slow = fast = i
            while True:
                slow = move(slow)
                fast = move(move(fast))
                if(slow ==fast and nums[slow] * nums[i] > 0):
                    return True
                if(slow ==fast or nums[slow] * nums[i] < 0):
                    break
        return False