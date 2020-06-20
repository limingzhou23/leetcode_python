#-*- coding:utf-8 -*-
#Author:李明洲
#python 3.7.3
#@Time:2020/6/6 9:52

import collections
# def longestConsecutive(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     s = set(nums)
#     res = 0
#     for num in nums:
#         if num - 1 in s:
#             continue
#         curLen = 1
#         print(num)
#
#         while num + 1 in s:
#             curLen += 1
#             num += 1
#         res = max(res, curLen)
#     return res

class DSU:
    def __init__(self, nums):
        self.pre = {num: num for num in nums}
        self.rank = collections.defaultdict(lambda: 1)
        self.cnt = collections.defaultdict(lambda: 1)

    #找到最高级的父亲
    def find(self, x):
        while x != self.pre[x]:
            x = self.pre[x]
        return x
    #合并两个结点
    def merge(self, x, y):
        if y not in self.pre:
            return 1
        root1, root2 = self.find(x), self.find(y)
        print(root1,root2)
        if root1 == root2:
            return self.cnt[root1]
        if self.rank[root1] < self.rank[root2]:
            self.pre[root1] = root2
            self.cnt[root2] += self.cnt[root1]
            return self.cnt[root2]
        elif self.rank[root1] > self.rank[root2]:
            self.pre[root2] = root1
            self.cnt[root1] += self.cnt[root2]
            return self.cnt[root1]
        else:
            self.pre[root1] = root2
            self.cnt[root2] += self.cnt[root1]
            self.rank[root2] += 1
            return self.cnt[root2]

def longestConsecutive(nums):
    dsu = DSU(nums)
    res = 0
    for num in nums:
        res = max(res, dsu.merge(num, num + 1))

    return res

nums=[100,4,200,1,3,2,55]
#print(longestConsecutive(nums))

def isPalindrome(x):
    if x<0 or (x%10 == 0 and x !=0):
        return False

    reversenum=0
    while x>reversenum :
        a=x%10
        x=x//10
        print(a)
        reversenum = reversenum*10+a
    print(reversenum)
    return x == reversenum or x== reversenum//10

#print(isPalindrome(11234))
print(isPalindrome(10))

