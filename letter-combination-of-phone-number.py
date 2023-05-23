"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.




Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        mapping = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }

        inputs = [int(i) for i in digits]
        output = []

        if len(inputs) == 0:
            return []

        output = mapping[inputs[0]]

        for i in range(1, len(inputs)):
            temp = []
            for x in output:
                for k in mapping[inputs[i]]:
                    temp.append(x + k)

            output = temp

        return output


s = Solution()
res = s.letterCombinations("234")
print(res)