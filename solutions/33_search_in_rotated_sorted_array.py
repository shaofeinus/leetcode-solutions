class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def search_start_index(nums, left_i, right_i):
            if left_i + 1 == right_i:
                return left_i if nums[left_i] < nums[right_i] else right_i
            if nums[left_i] < nums[right_i]:
                return left_i
            middle_i = (left_i + right_i) // 2
            if nums[left_i] > nums[middle_i]:
                return search_start_index(nums, left_i, middle_i)
            else:
                return search_start_index(nums, middle_i, right_i)

        def transform_to_actual_i(i, start_i, length):
            return (i + start_i) % length

        def bin_search(nums, target, left_i, right_i, start_i):
            left_i_a = transform_to_actual_i(left_i, start_i, len(nums))
            right_i_a = transform_to_actual_i(right_i, start_i, len(nums))

            if nums[left_i_a] == target:
                return left_i_a
            if nums[right_i_a] == target:
                return right_i_a
            if left_i + 1 == right_i:
                if nums[left_i_a] == target:
                    return left_i_a
                elif nums[right_i_a] == target:
                    return right_i_a
                else:
                    return -1

            middle_i = (left_i + right_i) // 2
            if target < nums[transform_to_actual_i(middle_i, start_i, len(nums))]:
                return bin_search(nums, target, left_i, middle_i, start_i)
            else:
                return bin_search(nums, target, middle_i, right_i, start_i)

        last_i = len(nums) - 1
        if last_i == -1:
            return -1
        elif last_i == 0:
            return 0 if nums[last_i] == target else -1
        else:
            return bin_search(nums, target, 0, last_i, search_start_index(nums, 0, last_i))


print(Solution().search([1], 0))
