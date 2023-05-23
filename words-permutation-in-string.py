"""
Given a string S and a dictionary containing a list of words, write a function to break the string completely into valid words.
Print all such possible sentences. The same word in the dictionary may be reused multiple times.

Example:
S = "catsanddog"
dictionary = ["cat", "cats", "and", "sand", "dog"]

Output:
"cat" "sand" "dog"
"cats" "and" "dog"
"""

class Solution(object):
    def permutations(self, input, dictionary):
        result = []
        self.find_words(input, [], dictionary, result)
        return result

    def find_words(self, input, partial, dictionary, result):
        if len(input) == 0:
            result.append(partial)
            return

        for i in range(1, len(input) + 1):
            subs = input[:i]
            if subs in dictionary:
                self.find_words(input[i:], partial + [subs], dictionary, result)


s = Solution()
res = s.permutations("catsanddog", ["cat", "cats", "and", "sand", "dog"])
print(res)