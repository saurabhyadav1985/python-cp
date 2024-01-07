'''
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''


class Solution:
    def search(nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # If the left half is not sorted, then the right half must be sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


    # Example usage:
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = search(nums, target)
    print(result)

'''
In this modified binary search, we determine which half of the array is sorted and check if the target value lies within that sorted half. If it does, we adjust the search range accordingly. If the target is not in the sorted half, we search the other half.

This approach maintains the logarithmic time complexity of O(log n) because, at each step, we eliminate half of the remaining elements in the search range.


The time complexity of the provided algorithm is O(log n), where n is the number of elements in the array.

Explanation:

The algorithm uses a binary search approach, which halves the search space in each iteration.
In the worst case, the entire array is considered in the search space, and the algorithm eliminates half of the remaining elements in each step.
Therefore, the time complexity is logarithmic with respect to the size of the array, resulting in O(log n) time complexity.
The space complexity is O(1), as the algorithm uses only a constant amount of extra space for variables like left, right, and mid.
'''
