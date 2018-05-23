class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums = sorted(nums, reverse=True)
        length = len(nums)
        quads = []
        prev_n_i = None

        # Generate a number index
        num_index = {}
        for i in range(length):
            n = nums[i]
            if num_index.get(n) is None:
                num_index[n] = [i]
            else:
                num_index[n].append(i)

        for i in range(length - 3):

            curr_n_i = nums[i]

            if target - curr_n_i * 4 > 0:
                # Cannot meet target even with max remaining numbers
                break

            if prev_n_i is not None and prev_n_i == curr_n_i:
                continue
            prev_n_i = curr_n_i
            prev_n_j = None

            for j in range(i + 1, length - 2):

                curr_n_j = nums[j]

                if target - curr_n_i - curr_n_j * 3 > 0:
                    # Cannot meet target even with max remaining numbers
                    break

                if prev_n_j is not None and prev_n_j == curr_n_j:
                    continue
                prev_n_j = curr_n_j
                prev_n_k = None

                for k in range(j + 1, length - 1):

                    curr_n_k = nums[k]

                    if target - curr_n_i - curr_n_j - curr_n_k * 2 > 0:
                        # Cannot meet target even with max remaining numbers
                        break

                    if prev_n_k is not None and prev_n_k == curr_n_k:
                        continue
                    prev_n_k = curr_n_k

                    last_num = target - curr_n_i - curr_n_j - curr_n_k
                    last_nun_indexes = num_index.get(last_num)
                    if last_nun_indexes is not None and last_nun_indexes[len(last_nun_indexes) - 1] > k:
                        # Last number has index after k
                        quads.append((curr_n_i, curr_n_j, curr_n_k, last_num))

        return quads


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
