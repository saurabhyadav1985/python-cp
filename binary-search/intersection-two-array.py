'''
49. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''
class Solution:
    def intersection(self, nums1, nums2):
        # Create two hash sets to store unique elements
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find the intersection by using the 'intersection' method of sets
        result = set1.intersection(set2)
        
        # Return the intersection as a list
        return list(result)

'''
Approach:

The problem requires finding the intersection of two arrays, nums1 and nums2.
To solve it, we can utilize hash sets.
First, we create two hash sets, set1 and set2, to store the unique elements of nums1 and nums2.
Next, we use the intersection method of sets to find the common elements between the two hash sets.
Finally, we convert the resulting set back into a list and return it as the required intersection.
Complexity Analysis:

The time complexity of this approach is O(n + m), where n and m are the lengths of nums1 and nums2 respectively. Constructing the hash sets takes O(n + m) time, and finding the intersection runs in O(min(n, m)) time.
The space complexity is O(min(n, m)), as it depends on the smaller of the two arrays. This accounts for the space used by the hash sets and the resulting intersection list.
'''