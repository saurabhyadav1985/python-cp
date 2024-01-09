#1040. Moving Stones Until Consecutive II

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
    
        # Calculate the maximum moves
        max_moves = max(stones[-1] - stones[1] - n + 2, stones[-2] - stones[0] - n + 2)
    
        # Calculate the minimum moves
        min_moves = float('inf')
        i, j = 0, 0
    
        while j < n:
            while stones[j] - stones[i] >= n:
                i += 1
        
            if j - i + 1 == n - 1 and stones[j] - stones[i] == n - 2:
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - (j - i + 1))
        
            j += 1
    
        return [min_moves, max_moves]

'''
The time complexity of the provided solution is O(n log n), where n is the number of stones. This is because the solution begins with sorting the array of stone positions, which has a time complexity of O(n log n). The subsequent calculations involve iterating through the sorted array, which takes linear time O(n).

The space complexity of the solution is O(1) since the algorithm uses a constant amount of extra space regardless of the input size. This is because the sorting is done in-place and no additional data structures are used that scale with the input size.

Sort the Stones:

The first step is to sort the array of stone positions (stones).
This is done using the sort() function in Python, which has a time complexity of O(n log n).
Calculate Maximum Moves:

Calculate the maximum number of moves (max_moves) by considering the scenarios where you move stones from the endpoints.
Two cases are considered:
Moving the rightmost stone to the leftmost empty position.
Moving the leftmost stone to the rightmost empty position.
The maximum moves formula is max(stones[-1] - stones[1] - n + 2, stones[-2] - stones[0] - n + 2).
Calculate Minimum Moves:

Calculate the minimum number of moves (min_moves) by iterating through the sorted array.
Use two pointers (i and j) to slide through the array.
The goal is to find a consecutive subarray of length n-1 (excluding one stone) since the game ends when the stones are in three consecutive positions.
While iterating, update min_moves based on different scenarios:
If there is a gap of exactly n-2 between stones, then it takes 2 moves to fill the gap.
Otherwise, calculate the number of moves needed to fill the gap between i and j positions.
Update min_moves as the minimum of the calculated moves or n - (j - i + 1).
Increment j to consider the next subarray.
Return Result:

Return the result as a list [min_moves, max_moves].
The algorithm ensures that the stones are moved to minimize and maximize the number of moves according to the given rules. Sorting the array allows for efficient calculations during the iteration process.
'''