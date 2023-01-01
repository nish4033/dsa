class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve_1(self, A, B):
        min_cost = float('inf')
        for i in range(0, len(A) - 3 + 1):
            for j in range(i + 1, len(A) - 2 + 1):
                for k in range(j + 1, len(A)):
                    if B[i] + B[j] + B[k] <= min_cost and A[i] < A[j] < A[k]:
                        min_cost = B[i] + B[j] + B[k]
        if min_cost == float("inf"):
            min_cost = -1
        return min_cost


A = [100, 101, 100]
B = [2, 4, 5]
s = Solution()
print(s.solve_1(A, B))
