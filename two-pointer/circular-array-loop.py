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
Time Complexity:

The outer for loop iterates over each index in the nums list, which takes O(n) time, where n is the size of the list.
Inside the for loop, the while loop runs until it breaks, which happens in one of two cases: a unicycle is detected (prev == i) or there is a sign difference between nums[prev] and nums[i].
In the worst case scenario, the while loop iterates up to n times, considering all elements are part of a single cycle. However, in practice, the while loop typically iterates much fewer times, depending on the structure of the input.
Therefore, the overall time complexity is O(n) in the worst case.
Space Complexity:

The algorithm uses a few sets (visited and cycle_set) to keep track of visited indices. The maximum number of elements that can be stored in these sets is bounded by the size of the input, so the space complexity is O(n), where n is the size of the input list nums.
Additionally, a few variables like size and prev are used, but they take constant space regardless of the input size.
Hence, the overall space complexity is O(n).

'''
    
    def circularArrayLoop(nums):
        def move(i):
        return (i + nums[i]) % len(nums)

    for i in range(len(nums)):
        slow = fast = i
        while True:
            slow = move(slow)
            fast = move(move(fast))
            if slow == fast and nums[slow] * nums[i] > 0:
                return True
            if slow == fast or nums[slow] * nums[i] < 0:
                break
    return False

'''
Time Complexity: The algorithm uses the Floyd's cycle-finding algorithm to detect cycles in the array. In the worst case scenario, the algorithm visits each index in the array once, and for each index, it traverses a part of the cycle. Therefore, the overall time complexity is O(n), where n is the size of the input array nums.

Space Complexity: The algorithm uses only a constant amount of extra space, independent of the size of the input array. Hence, the space complexity is O(1).'''