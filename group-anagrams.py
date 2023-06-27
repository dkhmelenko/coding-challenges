"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        results = []

        while len(strs) > 0:
            temp_res = []
            self.find_anagram(strs[0], strs, temp_res, "", strs[0])
            results.append(temp_res)
        return results

    def find_anagram(self, item, strs, results, partial, origin):
        if partial in strs and len(partial) == len(origin):
            count = strs.count(partial)
            for i in range(count):
                results.append(partial)
                strs.remove(partial)
            return

        for i in range(len(item)):
            new_item = item[:i] + item[i + 1:]
            sub = item[i]
            self.find_anagram(new_item, strs, results, partial + sub, origin)




s = Solution()
res = s.groupAnagrams(["bdddddddddd","bbbbbbbbbbc"])
print(res)
