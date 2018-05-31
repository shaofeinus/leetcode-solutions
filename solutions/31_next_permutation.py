class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        if length == 0 or length == 1:
            return

        # Find the first peak from back
        peak_i = 0
        for i in range(length - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                peak_i = i
                break

        if peak_i == 0:
            # Peak is first number, sort nums in asc order
            nums.sort()
        else:
            swap_i = None
            # Find smallest number that is bigger than number before peak and swap
            for i in range(length - 1, peak_i - 1, -1):
                if nums[i] > nums[peak_i - 1]:
                    swap_i = i
                    break
            temp = nums[swap_i]
            nums[swap_i] = nums[peak_i - 1]
            nums[peak_i - 1] = temp
            # Sort numbers behind peak index
            nums[peak_i:length] = sorted(nums[peak_i:length])


nums = [3, 2, 1]
Solution().nextPermutation(nums)
print(nums)
