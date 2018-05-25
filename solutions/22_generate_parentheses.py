class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def gen(left, right, curr, results):
        	if left == 0 and right == 0:
        		results.append(curr)
        	elif left == 0:
        		# Only can put right
        		gen(left, right - 1, curr + ')', results)
        	elif left == right:
        		# Only can put left
        		gen(left - 1, right, curr + '(', results)
        	else:
        		# Can put both left and right
        		gen(left - 1, right, curr + '(', results)
        		gen(left, right - 1, curr + ')', results)

        results = []
        gen(n, n, '', results)
        return results



