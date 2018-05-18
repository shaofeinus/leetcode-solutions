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
        if len(zeros) > 0:
            positives.append(0)
            negatives.append(0)

        result = {}
        # Put 3 zeros first
        if len(zeros) >= 3:
            self.put_in_result(0, 0, 0, result)

        # 1 positive, 2 negative
        self.search(positives, negatives, result, -1)
        # 1 negative, 2 positives
        self.search(negatives, positives, result, 1)

        real_result = list()
        for n_1 in result.keys():
            for n_2 in result[n_1].keys():
                real_result.append((n_1, n_2, result[n_1][n_2]))

        return real_result

    def search(self, nums, counter_nums, result, counter_num_sign):
        if len(counter_nums) < 2:
            # If only 1 counter num, impossible to form 3 numbers
            return

        num_tried = set()

        i_1, i_2 = 0, 1
        prev_1, prev_2 = counter_nums[i_1] + counter_num_sign, counter_nums[i_2] + counter_num_sign
        i_limit = len(counter_nums)
        for num in nums:
            if num == 0:
                break
            if num in num_tried:
                continue
            while i_2 < i_limit:
                curr_1, curr_2 = counter_nums[i_1], counter_nums[i_2]
                if curr_1 == prev_1 and curr_2 == prev_2:
                    # Repeat pair, try next pair
                    i_1, i_2 = self.next_i(i_1, i_2, i_limit)
                    continue
                state = num + curr_1 + curr_2
                if state == 0:
                    self.put_in_result(num, curr_1, curr_2, result)
                    i_1, i_2 = self.next_i(i_1, i_2, i_limit)
                    prev_1, prev_2 = curr_1, curr_2
                elif (num > 0 > state) or (num < 0 < state):
                    # Sum of counter numbers over compensate number. Try smaller counter numbers
                    i_1, i_2 = self.next_i(i_1, i_2, i_limit)
                    prev_1, prev_2 = curr_1, curr_2
                elif (num > 0 and state > 0) or (num < 0 and state < 0):
                    # The largest counter number cannot make number change sign. Try smaller number
                    break
            num_tried.add(num)

    def next_i(self, i_1, i_2, i_limit):
        if i_2 + 1 == i_limit:
            return i_1 + 1, i_1 + 2
        else:
            return i_1, i_2 + 1

    def put_in_result(self, num_1, num_2, num_3, result):

        def is_in_result(n_1, n_2, n_3):
            return n_1 in result and n_2 in result[n_1] and result[n_1][n_2] == n_3

        if is_in_result(num_1, num_2, num_3) or \
                is_in_result(num_1, num_3, num_2) or \
                is_in_result(num_2, num_1, num_3) or \
                is_in_result(num_2, num_3, num_1) or \
                is_in_result(num_3, num_1, num_2) or \
                is_in_result(num_3, num_2, num_1):
            return

        inner = result.get(num_1, {})
        inner[num_2] = num_3
        result[num_1] = inner


print(Solution().threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
