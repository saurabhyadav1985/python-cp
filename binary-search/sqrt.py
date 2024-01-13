'''
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python. 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

To solve the problem of finding the square root of a non-negative integer x and rounding it down to the nearest integer, you can use the binary search algorithm. Here's an implementation in Python:
'''

def mySqrt(x):
    if x == 0:
        return 0

    left, right = 1, x

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

    return -1  # unreachable

'''
Approach Explanation:

Edge case: If x is 0, return 0 since the square root of 0 is 0.
Initialize the search range using two pointers, left and right, with left as 1 and right as x.
Use binary search to find the square root within the search range.
In each iteration, calculate the mid as the average of left and right. Check if mid * mid is equal to x or if x lies between mid * mid and (mid + 1) * (mid + 1). If either condition is true, return mid as the square root of x.
If mid * mid is greater than x, update the right pointer to mid - 1 to search in the lower range. Otherwise, update the left pointer to mid + 1 to search in the higher range.
Repeat steps 4-5 until left is greater than right.
If no square root is found (unreachable), return -1.

Time Complexity: The time complexity of the algorithm is O(log n), where n is the given non-negative integer x. This is because the binary search algorithm reduces the search range in half in each iteration.

Space Complexity: The space complexity of the algorithm is O(1) since it only uses a constant amount of space for the pointers and variables.

Alternative Approaches and Their Complexity:

Newton's Method (Iterative):

Time Complexity: O(log n) - Convergence rate is quadratic, providing faster convergence compared to the binary search approach.
Space Complexity: O(1) - Requires a constant amount of additional space.
Babylonian Method (Iterative):

Time Complexity: O(log n) - Similar to Newton's method, it has a fast convergence rate.
Space Complexity: O(1) - Requires a constant amount of additional space.
Binary Search (Recursive):

Time Complexity: O(log n) - Halves the search range in each recursive call.
Space Complexity: O(log n) - Utilizes additional stack space due to the recursive calls.

'''
    
    