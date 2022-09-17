"""
Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.


Input Format

The only argument given is string A.
Output Format

Return the length of the longest consecutive 1’s that can be achieved.
Constraints

1 <= length of string <= 1000000
A contains only characters 0 and 1.
For Example

Input 1:
    A = "111000"
Output 1:
    3

Input 2:
    A = "111011101"
Output 2:
    7
"""


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        ans = 0
        count = 0
        if len(A) * "0" == A:
            return 0
        for i in A:
            if i == "1":
                count += 1
        if count == len(A):
            return count
        for i in range(len(A)):
            l_count = 0
            r_count = 0
            if A[i] == "0":
                for j in range(i - 1, -1, -1):
                    if A[j] == "1":
                        l_count += 1
                    else:
                        break
                for k in range(i + 1, len(A)):
                    if A[k] == "1":
                        r_count += 1
                    else:
                        break
                if count > l_count + r_count:
                    max_value = l_count + r_count + 1
                else:
                    max_value = l_count + r_count
                if max_value > ans:
                    ans = max_value

        return ans

s = Solution()
print(s.solve("00000011111111"))