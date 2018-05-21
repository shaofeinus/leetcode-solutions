class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def get_repeated_nums(nums):
            repeated_set = set()
            prev = nums[0]
            for curr in nums[1:]:
                if curr == prev:
                    repeated_set.add(curr)
                prev = curr
            return repeated_set

        def add_sums_of_unique_nums(unique_nums, sums):
            for i in range(len(unique_nums) - 1):
                for j in range(i + 1, len(unique_nums)):
                    n_1, n_2 = unique_nums[i], unique_nums[j]
                    added = n_1 + n_2
                    if sums.get(added) is None:
                        sums[added] = [(n_1, n_2)]
                    else:
                        sums[added].append((n_1, n_2))

        def add_sums_of_repeated_nums(repeated_nums, sums):
            for n in repeated_nums:
                added = n * 2
                if sums.get(added) is None:
                    sums[added] = [(n, n)]
                else:
                    sums[added].append((n, n))

        def search(unique_nums, counter_nums, triplets):
            if len(counter_nums) < 2:
                # Less then 2 counter nums, impossible to form 3 numbers
                return
            unique_counter_nums = list(set(counter_nums))
            repeated_counter_nums = list(get_repeated_nums(counter_nums))
            sums = {}
            add_sums_of_unique_nums(unique_counter_nums, sums)
            add_sums_of_repeated_nums(repeated_counter_nums, sums)
            for unique_num in unique_nums:
                pairs = sums.get(-unique_num)
                if pairs is not None:
                    triplets.extend([(unique_num, pair[0], pair[1]) for pair in pairs])

        def get_unique_triplets(triplets):
            triplets_dict = {}
            unique_triples = list()
            for triplet in triplets:
                n_1, n_2, n_3 = triplet[0], triplet[1], triplet[2]
                if triplets_dict.get(n_1, {}).get(n_2, {}).get(n_3) is None \
                        and triplets_dict.get(n_1, {}).get(n_3, {}).get(n_2) is None \
                        and triplets_dict.get(n_2, {}).get(n_1, {}).get(n_3) is None \
                        and triplets_dict.get(n_2, {}).get(n_3, {}).get(n_1) is None \
                        and triplets_dict.get(n_3, {}).get(n_1, {}).get(n_2) is None \
                        and triplets_dict.get(n_3, {}).get(n_2, {}).get(n_1) is None:
                    # Unique triplet
                    unique_triples.append((n_1, n_2, n_3))
                    if triplets_dict.get(n_1) is None:
                        triplets_dict[n_1] = {n_2: {n_3: True}}
                    elif triplets_dict[n_1].get(n_2) is None:
                        triplets_dict[n_1][n_2] = {n_3: True}
                    else:
                        triplets_dict[n_1][n_2][n_3] = True
            return unique_triples

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

        result = []
        # Put 3 zeros first
        if len(zeros) >= 3:
            result.append((0, 0, 0))

        # 1 positive, 2 negative
        search(list(set(positives)), negatives, result)
        # 1 negative, 2 positives
        search(list(set(negatives)), positives, result)

        return get_unique_triplets(result)


print(Solution().threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
