#80. Remove Duplicates from Sorted Array II

def removeDuplicates(nums):
    if not nums:
        return 0

    # Initialize pointers
    slow = 2
    for fast in range(2, len(nums)):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1

    return slow

# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = removeDuplicates(nums)
print(k)  # Output: 5
print(nums[:k])  # Elements up to index k in nums contain the final result

'''
To solve this problem, you can use two pointers to iterate through the array and remove duplicates. The idea is to check if the current element is equal to the previous two elements. If not, you can keep the element in the array. If yes, then it means there are already two instances of this element, and you should skip it.

The time complexity of the algorithm is O(n), where n is the length of the input array nums. The algorithm makes a single pass through the array with two pointers (slow and fast), and in each iteration, it performs constant-time operations.

The space complexity is O(1) since the algorithm uses only a constant amount of extra memory for the two pointers (slow and fast). The modifications are done in-place, without requiring additional data structures.
'''