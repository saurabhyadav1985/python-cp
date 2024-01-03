#845. Longest Mountain in Array

def longest_mountain(arr):
    n = len(arr)
    result = 0

    for i in range(1, n - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            left, right = i - 1, i + 1

            while left > 0 and arr[left - 1] < arr[left]:
                left -= 1

            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1

            result = max(result, right - left + 1)

    return result

# Example usage:
arr1 = [2, 1, 4, 7, 3, 2, 5]
arr2 = [2, 2, 2]

output1 = longest_mountain(arr1)
output2 = longest_mountain(arr2)

'''
This function longest_mountain takes an array arr as input and returns the length of the longest mountain subarray. It iterates through the array and identifies potential mountain peaks (arr[i] > arr[i-1] and arr[i] > arr[i+1]). For each potential peak, it expands to the left and right to find the complete mountain subarray and updates the result if a longer mountain is found.

The time complexity of the provided algorithm for finding the length of the longest mountain subarray is O(N), where N is the length of the input array arr.

Explanation:

The algorithm iterates through the array once using a single loop (for i in range(1, n - 1)), where 'n' is the length of the array.
In each iteration, the algorithm performs a constant amount of work, including checks and while loop operations that move pointers left and right.
Therefore, the overall time complexity is linear with respect to the size of the input array, making it O(N). The space complexity of the algorithm is O(1), as it uses a constant amount of additional space regardless of the input size.
'''