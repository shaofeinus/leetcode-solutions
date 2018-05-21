class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def search_closest(ns, value):
            left, right = 0, len(ns) - 1
            middle = (left + right) // 2
            while middle > left:
                n = ns[middle]
                if n > value:
                    # n too big
                    right = middle
                elif n < value:
                    # n too small
                    left = middle
                else:
                    return n
                middle = (left + right) // 2

            if left == right:
                # 1 number left
                return ns[left]
            else:
                # 2 numbers left, take the closer one
                n_1, n_2 = ns[left], ns[right]
                return n_1 if abs(value - n_1) < abs(value - n_2) else n_2

        nums = sorted(nums)
        closest = None
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                required = target - nums[i] - nums[j]
                closest_to_required = search_closest(nums[0:i] + nums[i + 1:j] + nums[j + 1:], required)
                result = nums[i] + nums[j] + closest_to_required
                if closest is None or abs(target - closest) > abs(target - result):
                    closest = result

        return closest


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
