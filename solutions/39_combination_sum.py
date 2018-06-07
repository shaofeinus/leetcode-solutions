class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def find_combi(curr_i, curr_sum, curr_combi, result):
            if curr_i < len(candidates):
                curr = candidates[curr_i]
                updated_sum = curr_sum + curr
                if updated_sum == target:
                    curr_combi.append(curr)
                    result.append(curr_combi)
                elif updated_sum < target:
                    curr_combi_copy_1 = curr_combi[:]
                    curr_combi_copy_1.append(curr)
                    curr_combi_copy_2 = curr_combi[:]
                    curr_combi_copy_2.append(curr)
                    find_combi(curr_i, updated_sum, curr_combi_copy_1, result)
                    find_combi(curr_i + 1, updated_sum, curr_combi_copy_2, result)
                else:
                    for i in range(curr_i + 1, len(candidates)):
                        if updated_sum + candidates[i] <= target:
                            curr_combi_copy_3 = curr_combi[:]
                            curr_combi_copy_3.append(curr)
                            find_combi(i, updated_sum, curr_combi_copy_3, result)

        candidates = sorted(candidates, reverse=True)

        result = list()
        for i in range(len(candidates)):
            find_combi(i, 0, list(), result)

        return result


print(Solution().combinationSum([2, 3, 5], 7))
