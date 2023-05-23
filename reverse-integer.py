class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        new_v = 0
        if x < 0:
            v = str(x)[1:][::-1]
            new_v = int(v) * -1
            if new_v < pow(2, 31) * -1:
                new_v = 0
        else:
            v = str(x)[::-1]
            new_v = int(v)
            if new_v > pow(2, 31) - 1:
                new_v = 0

        return new_v


s = Solution()
s.reverse(-123)