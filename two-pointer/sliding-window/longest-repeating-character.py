#424. Longest Repeating Character Replacement

def longest_substring(s, k):
    max_length = 0
    max_count = 0
    char_count = {}

    start = 0

    for end in range(len(s)):
        char_count[s[end]] = char_count.get(s[end], 0) + 1
        max_count = max(max_count, char_count[s[end]])

        # If the total number of characters in the current window minus the max_count
        # exceeds k, then we need to shrink the window.
        while (end - start + 1 - max_count) > k:
            char_count[s[start]] -= 1
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length

# Example usage:
s = "ABAB", k = 2
result = longest_substring(s, k)
print(result)  # Output: 4

'''
This function uses a sliding window to traverse the string while keeping track of the count of each character in the current window. The max_count variable stores the count of the most frequently occurring character in the current window. If the total number of characters in the current window minus max_count exceeds the allowed changes k, the window is shrunk from the left side. The maximum length of the substring is updated during each iteration. Finally, the function returns the maximum length of the substring containing the same letter after at most k changes.

The time complexity of the provided algorithm is O(n), where n is the length of the input string 's'. This is because the algorithm uses a sliding window approach with two pointers (start and end) to traverse the string once.

In the worst case, each character in the string is visited twice (once by the end pointer and once by the start pointer). The inner while loop, used to shrink the window when needed, ensures that each character is processed at most twice. Therefore, the overall time complexity is linear with respect to the length of the input string.

The space complexity of the algorithm is O(1) because the extra space used (such as the dictionary 'char_count') is bounded by a constant number of characters in the English alphabet. The space required does not grow with the size of the input.
'''
