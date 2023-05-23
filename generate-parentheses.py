"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        results = []
        self.backtrack("", results, n, 0, 0)

        return results

    def backtrack(self, partial, results, n, opened, closed):
        if len(partial) == n * 2:
            results.append(partial)
            return

        if opened < n:
            self.backtrack(partial + "(", results, n, opened + 1, closed)
        if closed < opened:
            self.backtrack(partial + ")", results, n, opened, closed + 1)
