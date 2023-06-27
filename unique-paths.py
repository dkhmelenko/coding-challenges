"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cache = dict()
        res = self.find_path(1, 1, m, n, cache)
        return res

    def find_path(self, curr_m, curr_n, m, n, cache):
        if curr_m == m and curr_n == n:
            return 1

        if curr_m > m or curr_n > n:
            return 0

        key = str([curr_m, curr_n])
        if key in cache:
            return cache[key]

        res = self.find_path(curr_m + 1, curr_n, m, n, cache) + self.find_path(curr_m, curr_n + 1, m, n, cache)
        cache[key] = res
        return res


s = Solution()
print(s.uniquePaths(23, 12))
