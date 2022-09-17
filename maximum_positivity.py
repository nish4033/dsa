"""Problem Description
Given an array of integers A, of size N.

Return the maximum size subarray of A having only non-negative elements. If there are more than one such subarray, return the one having the smallest starting index in A.

NOTE: It is guaranteed that an answer always exists.



Problem Constraints
1 <= N <= 105

-109 <= A[i] <= 109



Input Format
The first and only argument given is the integer array A.



Output Format
Return maximum size subarray of A having only non-negative elements. If there are more than one such subarrays, return the one having earliest starting index in A.



Example Input
Input 1:

 A = [5, 6, -1, 7, 8]
Input 2:

 A = [1, 2, 3, 4, 5, 6]


Example Output
Output 1:

 [5, 6]
Output 2:

 [1, 2, 3, 4, 5, 6]


Example
Explanation 1:

 There are two sub arrays of size 2 having only non-negative elements.
 1. [5, 6]  starting point  = 0
 2. [7, 8]  starting point  = 3
 As starting point of 1 is smaller, return [5, 6]
Explanation 2:

 There is only one subarray of size 6 having only non-negative elements:
 [1, 2, 3, 4, 5, 6]"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    @staticmethod
    def solve(a):
        res = []
        l_arr = []
        for l in range(len(a)):
            if a[l] >= 0:
                l_arr.append(a[l])
            else:
                break
        for i in range(len(a)):
            if a[i] < 0:
                r_arr = []
                for k in range(i + 1, len(a)):
                    if a[k] > 0:
                        r_arr.append(a[k])
                    else:
                        break

                if len(l_arr) >= len(r_arr):
                    res = l_arr
                else:
                    res = r_arr
                    l_arr = r_arr

        return res
s = Solution()
print(s.solve([ 7963262, 4011787, -833371, -1424649, -8187311, 6441214, -6071318, -7578657, -9536626, 7395028 ]))