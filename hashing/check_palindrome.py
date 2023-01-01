"""
Problem Description
Given a string A consisting of lowercase characters.

Check if characters of the given string can be rearranged to form a palindrome.

Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.



Problem Constraints
1 <= |A| <= 105

A consists only of lower-case characters.



Input Format
First argument is an string A.



Output Format
Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.



Example Input
Input 1:

 A = "abcde"
Input 2:

 A = "abbaee"


Example Output
Output 1:

 0
Output 2:

 1


Example Explanation
Explanation 1:

 No possible rearrangement to make the string palindrome.
Explanation 2:

 Given string "abbaee" can be rearranged to "aebbea" to form a palindrome.
"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        freq_dict = {}
        for i in A:
            if not freq_dict.get(i):
                freq_dict[i] = 1
            else:
                freq_dict[i] += 1
        if len(freq_dict) == 1:
            return 1
        N = len(A)
        single_element = 0
        c = set(A)
        for i in c:
            if N % 2 == 0:
                if freq_dict[i] % 2 != 0:
                    return 0
            else:
                if freq_dict[i] % 2 != 0:
                    single_element += 1
                    if single_element > 1:
                        return 0

        return 1


s = Solution()
print(s.solve("uucgncntt"))