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
Explaination1:
11 is represented as 1011 in binary.


"""


class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        if A % 2 == 0:
            count =0
        else:
            count = 1
        for _ in range(32):
            A = A >> 1
            if A % 2 == 1:
                count += 1
        return count

class Solution1:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        ret = 0
        while A != 0:
            # rightmost set bit becomes unset
            A = A & (A - 1)
            ret += 1
        return ret


s = Solution()
print(s.numSetBits(450676354))
