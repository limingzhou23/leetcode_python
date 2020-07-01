'''
-*- coding: utf-8 -*-
@Author  : 李明洲
@Time    : 2020/7/1 9:19
@Software: PyCharm
@File    : hashmap.py
'''

#718 最长重复子数组
class Solution:
    def findLength(self, A, B) :
        base, mod = 113, 10 ** 9 + 9

        def check(length) :
            hashA = 0
            for i in range(length):
                hashA = (hashA * base + A[i]) % mod
            print(hashA)
            bucketA = {hashA}
            mult = pow(base, length - 1, mod)
            for i in range(length, len(A)):
                hashA = ((hashA - A[i - length] * mult) * base + A[i]) % mod
                bucketA.add(hashA)

            hashB = 0
            for i in range(length):
                hashB = (hashB * base + B[i]) % mod
            if hashB in bucketA:
                return True
            for i in range(length, len(B)):
                hashB = ((hashB - B[i - length] * mult) * base + B[i]) % mod
                if hashB in bucketA:
                    return True

            return False

        left, right = 0, min(len(A), len(B))
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

A = [1,2,3,2,1]
B = [3,2,1,4,7]
solution = Solution()
ans = solution.findLength(A,B)
print((ans))