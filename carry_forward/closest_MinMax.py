"""
Problem Description
Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array

and at least one occurrence of the minimum value of the array.



Problem Constraints
1 <= |A| <= 2000



Input Format
First and only argument is vector A



Output Format
Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array



Example Input
Input 1:

A = [1, 3]
Input 2:

A = [2]


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation

Explanation 1:

 Only choice is to take both elements.
Explanation 2:

 Take the whole array.

"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_value = max(A)
        min_value = min(A)
        min_i = -1
        max_i = -1
        ans = 0
        for i in range(len(A) - 1, -1, -1):
            if A[i] == min_value:
                if max_i >= 0:
                    ans = max(ans, max_i - i + 1)
                min_i = i
            if A[i] == max_value:
                if min_i >= 0:
                    ans = max(ans, min_i - i + 1)
                max_i = i




        return ans

s = Solution()
print(s.solve([343, 291, 963, 165, 152]))