'''
153. Find Minimum in Rotated Sorted Array

Hint
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

Binary Search:

Perform a modified binary search to find the minimum element.
Compare the middle element with the leftmost and rightmost elements to determine which half of the array to search.
Continue dividing the search space in half until the minimum element is found.
Time Complexity: O(log n)
Space Complexity: O(1)

Linear Search:

Traverse the array sequentially and find the minimum element by comparing each element with its adjacent elements.
Time Complexity: O(n)
Space Complexity: O(1)
Approach Explanation: The problem requires finding the minimum element in a rotated sorted array in a time complexity of O(log n). 

The binary search approach is the most efficient and meets the required time complexity. It involves comparing the middle element of the array with the leftmost and rightmost elements. By comparing these values, it can be determined which half of the array to search. The search space is continuously divided in half until the minimum element is found. On the other hand, the linear search approach involves sequentially traversing the array and comparing each element with its adjacent elements until the minimum element is found. However, this approach has a higher time complexity of O(n).

Therefore, the binary search approach is recommended for finding the minimum element in a rotated sorted array due to its efficiency in terms of time complexity.
'''

def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


'''Explanation:

In the binary search approach, we initialize the left pointer to the start of the array (0) and the right pointer to the end of the array (len(nums) - 1).
We perform a binary search by updating the middle index (mid) in each iteration.
Check if the value at nums[mid] is greater than the value at nums[right]. If this condition is true, it means the minimum element is in the right half. Therefore, we update the left pointer to mid + 1.
If the condition is false, it means the minimum element is in the left half or nums[mid] could be the minimum element. We update the right pointer to mid.
Repeat steps 3 and 4 until the left pointer becomes equal to the right pointer.
Finally, return nums[left] as the minimum element in the rotated sorted array.
This binary search approach ensures a time complexity of O(log n), as it continually divides the search space in half by comparing the middle element with the rightmost element.
'''