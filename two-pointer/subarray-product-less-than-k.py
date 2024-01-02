713. Subarray Product Less Than K

def num_subarrays_with_product_less_than_k(nums, k):
    if k <= 1:
        return 0
    
    count = 0
    product = 1
    left = 0
    
    for right in range(len(nums)):
        product *= nums[right]
        
        while product >= k:
            product /= nums[left]
            left += 1
        
        count += right - left + 1
    
    return count

# Example usage:
nums1 = [10, 5, 2, 6]
k1 = 100
print(num_subarrays_with_product_less_than_k(nums1, k1))  # Output: 8

nums2 = [1, 2, 3]
k2 = 0
print(num_subarrays_with_product_less_than_k(nums2, k2))  # Output: 0

This function uses a sliding window with two pointers (left and right) to iterate through the array while maintaining the product of the elements in the current subarray. The while loop adjusts the window by moving the left pointer when the product becomes greater than or equal to k. The count is updated based on the valid subarrays encountered during the process.

The time complexity of the given algorithm is O(N), where N is the length of the input array nums. This is because each element is visited at most twice, once by the right pointer and once by the left pointer.

The space complexity is O(1), as the algorithm uses a constant amount of extra space regardless of the size of the input array. The extra space is used for variables like count, product, left, and right. The space required does not grow with the input size.