class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        pf_max = [A[0]]
        sf_max = [float("-inf")] * len(A)
        sf_max[-1] = A[-1]
        for i in range(1, len(A)):
            pf_max.append(max(pf_max[i - 1], A[i]))
        for j in range(len(A) - 2, -1, -1):
            sf_max[j] = max(sf_max[j + 1], A[j])
        ans = 0
        for i in range(1, len(A) - 1):
            water_height = min(pf_max[i - 1], sf_max[i + 1]) - A[i]
            if water_height > 0:
                ans += water_height
        return ans
s = Solution()
print(s.trap([0, 1, 0, 2]))