class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def get_repeated_set(num_list):
            repeated_set = set()
            prev = num_list[0]
            for curr in num_list[1:]:
                if curr == prev:
                    repeated_set.add(curr)
                prev = curr
            return repeated_set

        def is_unique_triplet(triplet, triplets_dict):
            n_1, n_2, n_3 = triplet[0], triplet[1], triplet[2]
            return triplets_dict.get(n_1, {}).get(n_2, {}).get(n_3) is None \
                and triplets_dict.get(n_1, {}).get(n_3, {}).get(n_2) is None \
                and triplets_dict.get(n_2, {}).get(n_1, {}).get(n_3) is None \
                and triplets_dict.get(n_2, {}).get(n_3, {}).get(n_1) is None \
                and triplets_dict.get(n_3, {}).get(n_1, {}).get(n_2) is None \
                and triplets_dict.get(n_3, {}).get(n_2, {}).get(n_1) is None

        def add_to_triplets_dict(triplet, triplets_dict):
            n_1, n_2, n_3 = triplet[0], triplet[1], triplet[2]
            if triplets_dict.get(n_1) is None:
                triplets_dict[n_1] = {n_2: {n_3: True}}
            elif triplets_dict[n_1].get(n_2) is None:
                triplets_dict[n_1][n_2] = {n_3: True}
            else:
                triplets_dict[n_1][n_2][n_3] = True

        def search(unique_nums, counter_nums, triplets, counter_num_sign, triplets_dict):
            if len(counter_nums) < 2:
                # Less then 2 counter nums, impossible to form 3 numbers
                return
            repeated_counter_nums = get_repeated_set(counter_nums)
            counter_nums_set = set(counter_nums)
            counter_nums = list(counter_nums_set)
            for num in unique_nums:
                for counter_num in counter_nums:
                    if abs(num) >= abs(counter_num):
                        other_counter_num = (abs(num) - abs(counter_num)) * counter_num_sign
                        if (other_counter_num == counter_num and counter_num in repeated_counter_nums) \
                                or (not other_counter_num == counter_num and other_counter_num in counter_nums_set):
                            triplet = (num, counter_num, other_counter_num)
                            if is_unique_triplet(triplet, triplets_dict):
                                triplets.append(triplet)
                                add_to_triplets_dict(triplet, triplets_dict)

        positives = []
        negatives = []
        zeros = []
        for n in nums:
            if n > 0:
                positives.append(n)
            elif n < 0:
                negatives.append(n)
            else:
                zeros.append(n)

        positives = sorted(positives, reverse=True)
        negatives = sorted(negatives)
        if len(zeros) > 0:
            positives.append(0)
            negatives.append(0)

        trs = []  # Triplets
        td = {}  # Triplet dicts
        # Put 3 zeros first
        if len(zeros) >= 3:
            trs.append((0, 0, 0))

        # 1 positive, 2 negative
        search(list(set(positives)), negatives, trs, -1, td)
        # 1 negative, 2 positives
        search(list(set(negatives)), positives, trs, 1, td)

        return trs


print(Solution().threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
