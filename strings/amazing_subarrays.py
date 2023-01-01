class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count = 0
        ans = 0
        vowel = ["a", "e", "i", "o", "u"]
        for i in A:
            if i.lower() in vowel:
                count += 1
            ans = ans + count
        return ans
s = Solution()
print(s.solve("pGpEusuCSWEaPOJmamlFAnIBgAJGtcJaMPFTLfUfkQKXeymydQsdWCTyEFjFgbSmknAmKYFHopWceEyCSumTyAFwhrLqQXbWnXSn"))
