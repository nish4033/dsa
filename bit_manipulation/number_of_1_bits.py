"""
Problem Description
Write a function that takes an integer and returns the number of 1 bits it has.


Problem Constraints
1 <= A <= 109


Input Format
First and only argument contains integer A


Output Format
Return an integer as the answer


Example Input
Input1:
11


Example Output
Output1:
3


Example Explanation

Explanation1:
11 is represented as 1011 in binary.
"""

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        res = ""
        count = 0
        while (A !=0):
            res = str(A % 2) + res
            A = A // 2
        for i in res:
            if i == "1":
                count += 1
        return count

