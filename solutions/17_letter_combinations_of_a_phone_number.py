class Solution:
    DIGIT_TO_LETTER_MAPPING = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        def add_combi_dfs(curr_digits, curr_chars, seqs):
            if len(curr_digits) == 0:
                seqs.append(''.join(curr_chars))
            else:
                for char in self.DIGIT_TO_LETTER_MAPPING[curr_digits[0]]:
                    new_curr_chars = curr_chars + char
                    add_combi_dfs(curr_digits[1:], new_curr_chars, seqs)

        if len(digits) == 0:
            return []

        result = []
        add_combi_dfs(digits, '', result)

        return result


print(Solution().letterCombinations(''))
