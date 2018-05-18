class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        positives = []
        negatives = []
        zeros = []
        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)
            else:
                zeros.append(num)

        positives = sorted(positives, reverse=True)
        negatives = sorted(negatives)

        result = []
        # Put n zeros first
        if len(zeros) >= 3:
            result.append((0, 0, 0))
        # 1 positive
        self.search(positives, negatives, result, len(zeros) > 0)
        # 1 negative
        self.search(negatives, positives, result, len(zeros) > 0)

        return result

    def search(self, nums, counter_nums, result, counter_has_zero):
        if len(counter_nums) < 2:
            # If only 1 counter num, impossible to form 3 numbers
            return

        i_1, i_2 = 0, 1
        i_limit = len(counter_nums)
        for num in nums:
            if num == 0:
                continue
            while i_2 < i_limit:
                state = num + counter_nums[i_1] + counter_nums[i_2]
                if state == 0:
                    result.append((num, counter_nums[i_1], counter_nums[i_2]))
                    i_1, i_2 = self.next_i(i_1, i_2, i_limit)
                elif (num > 0 and state < 0) or (num < 0 and state > 0):
                    # Sum of counter numbers over compensate number. Try smaller counter numbers
                    i_1, i_2 = self.next_i(i_1, i_2, i_limit)
                elif (num > 0 and state > 0) or (num < 0 and state < 0):
                    # The largest counter number cannot make number change sign. Try smaller number
                    break

    def next_i(self, i_1, i_2, i_limit):
        if i_2 + 1 == i_limit:
            return i_1 + 1, i_1 + 2
        else:
            return i_1, i_2 + 1


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
