"""
You are given an array A of non-negative numbers and a target sum S.
Write an efficient function that finds one continious sub-sequence of elements
which sum up to presicely sum S.

The return value should be a pair of array indices or an empty array
Example:
    input [1, 2, 3], target 5
    output [1, 2]
"""
def subsequenceSum(arr, targetSum):

    if len(arr) == 0:
        return []

    if len(arr) == 1 and arr[0] == targetSum:
        return [0]

    index_start = 0
    index_end = -1
    current_sum = arr[index_start]

    found_solution = False
    for i in range(1, len(arr)):
        current_sum = current_sum + arr[i]

        # curren sum < target sum
        if current_sum < targetSum:
            continue

        # current sum > target_sum
        if current_sum > targetSum:
            while index_start <= i:
                current_sum -= arr[index_start]
                index_start += 1

                if current_sum == targetSum:
                    found_solution = True
                    break
                if current_sum < targetSum:
                    break

        if current_sum == targetSum or found_solution:
            index_end = i
            break

    if index_end != -1:
        return [index_start, index_end]
    else:
        return []

res = subsequenceSum([2, 3, 1, 4, 2, 9], 7)
print(res)