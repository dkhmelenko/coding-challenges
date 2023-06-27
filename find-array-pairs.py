"""
Given a number K and an array of unique numbers N, write an application to find and print
all pairs in N that have an equal sum to K

Example:
Input:
K = 5
A = [1, 2, 3, 4, 5]

Output:
[2,3], [1,4]
"""
from typing import List


def find_pair_for_sum(expected_sum: int, array: List[int]) -> List[List[int]]:

    sorted_array = sorted(array)

    i = 0
    j = len(array) - 1

    results = []

    while i < j:
        current_sum = sorted_array[i] + sorted_array[j]

        if current_sum == expected_sum:
            results.append([sorted_array[i], sorted_array[j]])
            i += 1
            j -= 1

        if current_sum > expected_sum:
            j -= 1
        if current_sum < expected_sum:
            i += 1

    return results


def pairs_exist_in_array():
    K = 5
    A = [3, 2, 1, 4, 5]
    actual_result = find_pair_for_sum(K, A)
    expected_result = [[1,4], [2,3]]
    print(f"Actual result: {actual_result}")
    assert actual_result == expected_result


def no_pairs_found_in_array():
    K = 10
    A = [3, 2, 1, 4, 5]
    actual_result = find_pair_for_sum(K, A)
    expected_result = []
    print(f"Actual result: {actual_result}")
    assert actual_result == expected_result


def input_array_is_empty():
    K = 10
    A = []
    actual_result = find_pair_for_sum(K, A)
    expected_result = []
    print(f"Actual result: {actual_result}")
    assert actual_result == expected_result


def input_contains_float_numbers():
    K = 5
    A = [3.0, 2.0, 1.0, 4.0, 5.0]
    actual_result = find_pair_for_sum(K, A)
    expected_result = [[1.0, 4.0], [2.0, 3.0]]
    print(f"Actual result: {actual_result}")
    assert actual_result == expected_result


pairs_exist_in_array()
no_pairs_found_in_array()
input_array_is_empty()
input_contains_float_numbers()





