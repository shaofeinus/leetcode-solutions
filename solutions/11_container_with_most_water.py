class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        length = len(height)
        # List of height info
        height_info_list = [{'index': i, 'height': height[i]} for i in range(length)]
        # Sort list by height
        height_info_list = sorted(height_info_list, key=lambda item: item['height'], reverse=True)
        # Start with second highest height
        max_min_heights = [None] * length
        for i in range(1, length):
            prev_height_info = height_info_list[i - 1]
            curr_height_info = height_info_list[i]
            if i == 1:
                max_min_heights[i] = {
                    'max_i': prev_height_info['index'],
                    'min_i': prev_height_info['index'],
                    'height_info': curr_height_info
                }
            else:
                prev_max_min_height = max_min_heights[i - 1]
                max_min_heights[i] = {
                    'max_i': max(prev_height_info['index'], prev_max_min_height['max_i']),
                    'min_i': min(prev_height_info['index'], prev_max_min_height['min_i']),
                    'height_info': curr_height_info
                }

        max_area = 0
        for max_min_height in max_min_heights:
            if max_min_height is not None:
                max_area = max(
                    self.max_d(max_min_height['max_i'],
                               max_min_height['min_i'],
                               max_min_height['height_info']['index']) *
                    max_min_height['height_info']['height'],
                    max_area
                )

        return max_area

    def max_d(self, max_i, min_i, this_i):
        if this_i >= max_i:
            return this_i - min_i
        elif this_i <= min_i:
            return max_i - this_i
        else:
            return max(this_i - min_i, max_i - this_i)
