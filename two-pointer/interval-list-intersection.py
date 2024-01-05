#986. Interval List Intersections

def interval_intersection(firstList, secondList):
    result = []
    i, j = 0, 0

    while i < len(firstList) and j < len(secondList):
        start1, end1 = firstList[i]
        start2, end2 = secondList[j]

        # Check for overlapping intervals
        if end1 < start2:
            i += 1
        elif end2 < start1:
            j += 1
        else:
            # Calculate the intersection
            intersection_start = max(start1, start2)
            intersection_end = min(end1, end2)

            result.append([intersection_start, intersection_end])

            # Move the pointers to the next intervals
            if end1 < end2:
                i += 1
            else:
                j += 1

    return result

# Example usage:
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
output = interval_intersection(firstList, secondList)
print(output)

'''
This code defines a function interval_intersection that takes two lists of closed intervals as input and returns their intersection. The result is then printed for the given example.

The time complexity of the provided algorithm is O(N), where N is the total number of intervals in both firstList and secondList.

This is because each interval is examined once, and at each step, the algorithm either moves the pointer in the firstList or the secondList until one of the lists is exhausted. The algorithm compares intervals, calculates intersections, and moves pointers in a linear fashion, so its complexity is linear with respect to the total number of intervals.

The space complexity is O(1) since the algorithm uses a constant amount of extra space to store the pointers and the result list, and the space doesn't depend on the input size.
'''