"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        start = 0
        end = len(nums) - 1
        start_index = -1
        while start <= end:
            middle = int((start + end) / 2)
            if nums[middle] == target:
                start_index = middle
                end = middle - 1
            else:
                if target < nums[middle]:
                    end = middle - 1
                else:
                    start = middle + 1

        start = 0
        end = len(nums) - 1
        end_index = -1
        while start <= end:
            middle = int((start + end) / 2)

            if nums[middle] == target:
                end_index = middle
                start = middle + 1
            else:
                if target < nums[middle]:
                    end = middle - 1
                else:
                    start = middle + 1

        return [start_index, end_index]


s = Solution()
r = s.searchRange([5,7,7,8,8,10], 8)
print(r)