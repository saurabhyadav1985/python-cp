#441 "Arranging Coins":

class Solution:
    def arrangeCoins(self, n):
        # Using binary search to find the number of complete rows
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            curr = (mid * (mid + 1)) // 2
            
            if curr == n:
                return mid
            
            if curr < n:
                left = mid + 1
            else:
                right = mid - 1
        
        return right

'''
Approach:

To determine the number of complete rows in the staircase, we can use binary search.
We initialize two pointers, left and right, to represent the lower and upper bounds of the search range respectively.
While the left pointer is less than or equal to the right pointer:
Calculate the midpoint of the range using the formula (left + right) // 2.
Compute the number of coins that would be required to build mid rows using the formula curr = (mid * (mid + 1)) // 2.
Compare curr with the given number of coins n.
If curr is equal to n, we have found the exact number of complete rows, so we return mid.
If curr is less than n, we update left = mid + 1 to search for more rows.
If curr is greater than n, we update right = mid - 1 to reduce the number of rows in the search range.
Finally, we return the value of right, which represents the largest number of complete rows that can be built within the given number of coins.

Complexity Analysis:

The time complexity of the binary search approach is O(log n), where n is the given number of coins. The search range is halved at each step during the binary search.
The space complexity is O(1) since no extra space is used apart from the variables to store the indices and computations.

This solution efficiently determines the number of complete rows that can be built with the given number of coins by using binary search techniques.
'''