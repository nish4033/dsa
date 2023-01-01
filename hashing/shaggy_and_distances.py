class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        first_index = {}
        for i in range(len(A)):
            if first_index.get(A[i]) is None:
                first_index[A[i]] = i
        min_len = float("inf")
        for i in range(len(A)):
            if first_index[A[i]] != i:
                dis = abs(i - first_index[A[i]])
                if dis < min_len:
                    min_len = dis
        if min_len == float("inf"):
            min_len = -1
        return min_len


s = Solution()
print(s.solve([ 81760, 79550, 22559, 75299, 16955, 88462, 61786, 75867, 70648, 3369, 22975, 96532, 25025, 66395, 93487, 99745, 18113, 53612, 27186, 46537, 45321, 66174, 17988, 41507, 1917, 17613, 20118, 97218, 49013, 69220, 7583, 17748, 64613, 99073, 32976, 84997, 96961, 1757, 9565, 19937, 20844, 52727, 84400, 2459, 29910, 92266, 56997, 95895, 14078, 62465, 56931, 58056, 31338, 85194, 35782, 85090, 75386, 13941, 4115, 25904, 20784, 87872, 60888, 48447, 95087, 54725, 91079, 22263, 88947, 79672, 45292, 81355, 18933, 29522, 44401, 73426, 6301, 75670, 77769, 58508, 67734, 41227, 26015, 97582, 3651, 56043, 74721, 18679, 65400, 33055, 19979, 7691, 484, 93470, 40183, 67462, 81564, 99434, 4884, 38894 ]))