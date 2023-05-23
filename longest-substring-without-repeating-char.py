"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 1:
            return 1

        substr = ""
        maxLen = 0
        for i, el in enumerate(s):
            print(substr)
            if el in substr:
                substr = substr[substr.index(el) + 1:]
            substr = substr + el
            maxLen = max(maxLen, len(substr))

        return maxLen
