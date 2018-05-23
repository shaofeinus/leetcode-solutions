class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        length = len(nums)
        quads = []
        prev_n_i = None
        for i in range(length - 3):
            curr_n_i = nums[i]
            if prev_n_i is not None and prev_n_i == curr_n_i:
                continue
            prev_n_i = curr_n_i
            prev_n_j = None
            for j in range(i + 1, length - 2):
                curr_n_j = nums[j]
                if prev_n_j is not None and prev_n_j == curr_n_j:
                    continue
                prev_n_j = curr_n_j
                prev_n_k = None
                for k in range(j + 1, length - 1):
                    curr_n_k = nums[k]
                    if prev_n_k is not None and prev_n_k == curr_n_k:
                        continue
                    prev_n_k = curr_n_k
                    last_num = target - curr_n_i - curr_n_j - curr_n_k
                    if bin_search(nums, last_num, k + 1, length - 1):
                        quads.append((curr_n_i, curr_n_j, curr_n_k, last_num))

        return quads


def bin_search(nums, target, left, right):
    if left == right:
        return nums[left] == target

    if left + 1 == right:
        return nums[left] == target or nums[right] == target

    middle = (left + right) // 2
    n_middle = nums[middle]
    if n_middle == target:
        return True
    elif n_middle > target:
        return bin_search(nums, target, left, middle)
    else:
        return bin_search(nums, target, middle, right)


print(Solution().fourSum(
    [-492, -465, -454, -450, -416, -403, -384, -378, -377, -368, -360, -341, -325, -322, -315, -310, -309, -284, -275,
     -274, -271, -264, -255, -248, -245, -232, -222, -212, -211, -204, -184, -137, -133, -128, -120, -117, -109, -92,
     -88, -61, 19, 19, 32, 37, 39, 55, 60, 94, 98, 187, 187, 216, 254, 272, 284, 284, 290, 295, 323, 328, 336, 411, 428,
     440],
    1154))
