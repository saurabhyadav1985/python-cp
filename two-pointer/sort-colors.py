'''
75. Sort Colors


Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

'''

def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    
    return nums

# Example usage:
nums = [2, 0, 2, 1, 1, 0]
sorted_nums = sortColors(nums)
print(sorted_nums)

'''
This algorithm (Dutch national flag algorithm) uses three pointers (low, mid, and high) to partition the array into three sections: elements less than 1, elements equal to 1, and elements greater than 1. By swapping elements based on their values, the array is sorted in-place. 

The time complexity of the Dutch National Flag algorithm, as implemented above, is O(n), where n is the number of elements in the array. The algorithm makes a single pass through the array, and during each iteration, it either increments the mid pointer or swaps elements, both of which are constant-time operations.

The space complexity of the algorithm is O(1) since it uses only a constant amount of extra space for the three pointers (low, mid, and high).
'''