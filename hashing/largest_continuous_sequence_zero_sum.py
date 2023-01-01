"""
Problem Description
Given an array A of N integers.

Find the largest continuous sequence in a array which sums to zero.



Problem Constraints
1 <= N <= 106

-107 <= A[i] <= 107



Input Format
Single argument which is an integer array A.



Output Format
Return an array denoting the longest continuous sequence with total sum of zero.

NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.



Example Input
A = [1,2,-2,4,-4]


Example Output
[2,-2,4,-4]


Example Explanation
[2,-2,4,-4] is the longest sequence with total sum of zero.
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        prefix_array = []
        sum = 0
        for i in A:
            sum = sum + i
            prefix_array.append(sum)
        print(prefix_array)
        first_index = {0: -1}
        for i in range(len(prefix_array)):
            if first_index.get(prefix_array[i]) is None:
                first_index[prefix_array[i]] = i
        print(first_index)
        res = 0
        for i in range(len(prefix_array)):
            if first_index[prefix_array[i]] != i:
                res = 1
        return res


s = Solution()
print(s.lszero([ -1, 1 ] ))
