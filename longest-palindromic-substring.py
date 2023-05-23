"""
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 1:
            return 1

        collector = ""
        longest_palindrome = ""
        for i, c in enumerate(s):
            collector = ""
            for j in range(i, len(s)):
                collector = "".join([collector, s[j]])
                mid_stop = int(len(collector) / 2)
                mid_start = int(len(collector) / 2)
                if len(collector) % 2 == 1:
                    mid_stop += 1
                print(collector)

                if collector == collector[::-1]:
                # if collector[:mid_start] == collector[mid_stop:][::-1]:
                    if len(collector) > len(longest_palindrome):
                        longest_palindrome = collector

        return longest_palindrome


s = Solution()
res = s.longestPalindrome("cbbd")
print(f"Result {res}")