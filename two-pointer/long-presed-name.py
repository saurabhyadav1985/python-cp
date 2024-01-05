#925. Long Pressed Name

def isLongPressedName(name, typed):
    i, j = 0, 0

    while j < len(typed):
        if i < len(name) and name[i] == typed[j]:
            i += 1
            j += 1
        elif j > 0 and typed[j] == typed[j - 1]:
            j += 1
        else:
            return False

    return i == len(name)

# Example usage:
name1 = "alex"
typed1 = "aaleex"
print(isLongPressedName(name1, typed1))  # Output: True

'''
This function uses two pointers (i and j) to iterate through the characters of the name and typed strings. It compares characters and handles the long-pressed key scenario. The function returns True if it is possible that the typed characters match the friend's name.

The time complexity of the given algorithm is O(N + M), where N is the length of the name string and M is the length of the typed string. Both strings are traversed once using the two pointers (i and j).

The space complexity is O(1), as the algorithm uses only a constant amount of extra space for the two pointers and a few variables. The space used is independent of the input size.
'''