'''
96. Next Greater Element I
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
'''

def nextGreaterElement(nums1, nums2):
    # Create a dictionary to store the next greater element for each element in nums2
    next_greater = {}
    stack = []

    # Iterate through nums2 to find the next greater element for each element
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)

    # For elements left in the stack, there is no next greater element
    for num in stack:
        next_greater[num] = -1

    # Create the result array by looking up the next greater element for each element in nums1
    ans = [next_greater.get(num, -1) for num in nums1]
    
    return ans

# Example usage:
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
result = nextGreaterElement(nums1, nums2)
print(result)

'''
In this implementation, we use a stack to keep track of elements in nums2. We iterate through nums2, and for each element, we check if it is greater than the elements at the top of the stack. If it is, we update the next_greater dictionary for the elements popped from the stack. After the iteration, we handle the remaining elements in the stack and set their next greater element to -1.

Finally, we create the result array by looking up the next greater element for each element in nums1 using the next_greater dictionary.

The time complexity of the provided solution is O(N), where N is the total number of elements in nums2. This is because each element in nums2 is processed once in the worst case.

The space complexity is also O(N), as the stack and the next_greater dictionary both can potentially store all elements from nums2.
'''