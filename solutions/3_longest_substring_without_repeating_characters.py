class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        start_index = 0
        while start_index < len(s):
            curr_longest, start_index = self.longestSubstring(s, start_index)
            longest = max(curr_longest, longest)
        return longest

    def longestSubstring(self, s, start_index):
        curr_max = 0
        c_index_map = {}
        for i in range(start_index, len(s)):
            c = s[i]
            index = c_index_map.get(c, None)
            if index is None:
                curr_max += 1
                c_index_map[c] = i
            else:
                return curr_max, index + 1
        # Manage to find all the way till the end
        return curr_max, len(s) + 1
