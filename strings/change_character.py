class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A):
        vowels= "aeiou"
        B = A
        D = "".join([i for i in A if i.islower()])
        C = "".join([D.replace(i, "#") for i in A if i in vowels])

        return C + C


s = Solution()
print(s.solve(
    "ldfgbkldfgbk"))
