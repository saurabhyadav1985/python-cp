#88 Merge Sorted Array
def merge(nums1, m, nums2, n):
    # Initialize pointers for nums1 and nums2
    i, j, k = m - 1, n - 1, m + n - 1
    
    # Merge elements from the end of both arrays
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    # If there are remaining elements in nums2, copy them to nums1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)

print(nums1)

'''
You can merge the two sorted arrays in a way that takes advantage of their sorted nature. Since nums1 has enough space to accommodate both arrays, you can start from the end of both arrays and compare and merge the elements, placing them in the correct position in nums1.

The time complexity of the provided algorithm is O(m + n), where m is the length of the nums1 array and n is the length of the nums2 array. The algorithm iterates through both arrays once, and the number of iterations is proportional to the total number of elements in both arrays.

The space complexity of the algorithm is O(1), as it only uses a constant amount of extra space for the loop variables and temporary storage. The merging is done in-place, and the overall space required does not depend on the input size.
'''