class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        total_length = len(s)
        visited = [[False for x in range(total_length)] for y in range(total_length + 1)]
        for length in range(total_length, 0, -1):
            for start_index in range(0, total_length - length + 1):
                if self.search(s, length, start_index, visited):
                    return s[start_index:start_index + length]

        return s[0]

    def search(self, s, length, start_index, visited):
        if visited[length][start_index]:
            return False

        visited[length][start_index] = True

        if length <= 1:
            return True
        else:
            if s[start_index] == s[start_index + length - 1]:
                return self.search(s, length - 2, start_index + 1, visited)
            else:
                return False
