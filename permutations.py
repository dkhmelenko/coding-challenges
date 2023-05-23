"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.find_permutation(nums, [], result)
        return result

    def find_permutation(self, nums, partial, collector):
        if len(nums) == 0:
            collector.append(partial)
            return

        for i in range(len(nums)):
            new_elements = nums[:i] + nums[i+1:]
            curr_element = nums[i]
            self.find_permutation(new_elements, partial + [curr_element], collector)


s = Solution()
res = s.permute([1, 2, 3])
print(res)
