"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        self.transpose_matrix(matrix)
        print(matrix)
        self.swap_columns(matrix)

        return matrix

    def transpose_matrix(self, matrix):
        ranges = int(len(matrix))
        for i in range(ranges):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def swap_columns(self, matrix):
        ranges = int(len(matrix) / 2)
        for i in range(len(matrix)):
            for j in range(ranges):
                last_item = len(matrix) - j - 1
                matrix[i][j], matrix[i][last_item] = matrix[i][last_item], matrix[i][j]


s = Solution()
res = s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
print(res)