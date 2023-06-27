"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == 0:
                    for k in range(len(matrix[0])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = "a"
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0:
                            matrix[k][j] = "a"

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "a":
                    matrix[i][j] = 0


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s = Solution()
s.setZeroes(matrix)
print(matrix)