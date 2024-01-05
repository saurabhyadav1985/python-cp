def totalFruit(fruits):
    fruit_count = {}
    max_fruits = 0
    left = 0

    for right in range(len(fruits)):
        fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1

        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits

# Example usage:
fruits1 = [1, 2, 1]
print(totalFruit(fruits1))  # Output: 3

'''
This function uses a sliding window with two pointers (left and right). It keeps track of the count of each type of fruit in the window using a dictionary (fruit_count). The window expands to the right until it violates the rule of having only two types of fruit in the baskets, then it contracts from the left until the rule is satisfied again. The maximum number of fruits picked is updated during each iteration.

The time complexity of the given algorithm is O(N), where N is the number of elements in the input array fruits. This is because each element in the array is processed once by the two pointers (left and right), and the while loop inside the for loop also executes at most N times.

The space complexity is O(1), as the size of the fruit_count dictionary is at most 2 (representing the two types of fruits in the baskets). The space used for variables like left, right, and max_fruits is constant and does not depend on the size of the input.
'''