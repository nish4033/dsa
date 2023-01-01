"""
Problem Description
Implement pow(A, B) % C.
In other words, given A, B and C, Find (AB % C).

Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.



Problem Constraints
-109 <= A <= 109
0 <= B <= 109
1 <= C <= 109


Input Format
Given three integers A, B, C.


Output Format
Return an integer.


Example Input
A = 2, B = 3, C = 3


Example Output
2


Example Explanation
23 % 3 = 8 % 3 = 2
"""
import sys

sys.setrecursionlimit(10 ** 6)
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if B == 1:
            return A
        val = self.pow(A, B//2, C)
        val_1 = (val % C) * (val % C)
        if B % 2 ==0:
            return val_1 % C
        else:
            return (val_1 * A) % C

s = Solution()
print(s.pow(2, 3, 4))