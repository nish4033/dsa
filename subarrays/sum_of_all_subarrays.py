class Solution:
    # @param A : list of integers
     # @return an long
    def subarraySum(self, A):
        # total_sum = 0
        # for i in range(len(A)):
        #     sum_sub = 0
        #     for j in range(i, len(A)):
        #         sum_sub = sum_sub + A[j]
        #         total_sum = total_sum + sum_sub
        # return total_sum
        total_sum = 0
        for i in range(len(A)):
            total_sum = total_sum + A[i] * (len(A) - i)
        return total_sum


s = Solution()
print(s.subarraySum([2, 9, 5]))