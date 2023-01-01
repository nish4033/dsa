class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        max_len = max(len(A), len(B))

        A = A.zfill(max_len)
        B = B.zfill(max_len)

        ans = ""
        carry = 0
        for i in range(max_len - 1, -1, -1):
            sum_binary = int(A[i]) + int(B[i]) + carry
            carry = sum_binary // 2
            ans = str(sum_binary % 2) + ans
        return ans


A = "1010110111001101101000"
B = "1000011011000000111100110"
s = Solution()
print(s.addBinary(A, B))
