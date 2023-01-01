# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def plusOne(self, A):
#         place = 1
#         num = 0
#         for i in range(len(A) - 1, -1, -1):
#             num = num + A[i] * place
#             place = place * 10
#         print(num)
#         num = num + 1
#         ans = []
#         while num != 0:
#             ans.append(num % 10)
#             num = num // 10
#         ans.reverse()
#         return ans

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, a):
        ans = 0
        flag = 0
        for i in range(len(a)):
            if a[i] != 0:
                ans = i
                break
        for i in range(len(a) - 1, -1, -1):
            if a[i] == 9:
                a[i] = 0
                flag = 1
            else:
                a[i] += 1
                flag = 0
                break
        if flag == 1:
            a = [1] + a[ans:]
        else:
            a = [] + a[ans:]
        return a


s = Solution()
print(s.plusOne([0, 9, 9]))
