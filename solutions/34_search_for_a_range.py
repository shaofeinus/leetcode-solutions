class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def search(left, right, is_left):
            left_num = nums[left]
            right_num = nums[right]
            if is_left:
                # Check if found left boundary
                if left_num == target and (left == 0 or not nums[left - 1] == target):
                    return left
                elif right_num == target and not nums[right - 1] == target:
                    return right
            else:
                # Check if found right boundary
                if right_num == target and (right == len(nums) - 1 or not nums[right + 1] == target):
                    return right
                elif left_num == target and not nums[left + 1] == target:
                    return left

            # Continue search
            middle = (left + right) // 2

            if middle == left:
                # Already searched all
                return -1

            middle_num = nums[middle]
            if is_left:
                if middle_num >= target:
                    return search(left, middle, is_left)
                else:
                    return search(middle, right, is_left)
            else:
                if middle_num <= target:
                    return search(middle, right, is_left)
                else:
                    return search(left, middle, is_left)

        last_i = len(nums) - 1
        if last_i == -1:
            return -1, -1
        else:
            return search(0, last_i, True), search(0, last_i, False)


print(Solution().searchRange([], 1))
