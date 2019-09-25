
#Example answer: https://leetcode.com/problems/flipping-an-image/solution/
import numpy as np
class Solution(object):
    def flipAndInvertImage(self, A):
        for row in A:
            for i in np.arange((len(row) + 1) / 2):
                """
                In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                helps us find the i-th value of the row, counting from the right.
                """
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A

s = Solution()
A = [[1,1,0],[1,0,1],[0,0,0]]
print(s.flipAndInvertImage(A))

class Solution1: #https://leetcode.com/problems/flipping-an-image/discuss/325340/Python3-faster-than-98.47.-Understandable-method
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype : List[List[int]]
        """
        output = []
        for index, List in enumerate(A):
            List.reverse()
            targetList = [abs((x-1)) for x in List]
            output.append(targetList)
        return output

s1 = Solution1()
A = [[1,1,0],[1,0,1],[0,0,0]]
print(s1.flipAndInvertImage(A))
