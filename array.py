#-*- coding:utf-8 -*-
#Author:李明洲
#python 3.7.3
#@Time:2020/6/6 9:52

import bisect
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

# class DSU:
#     def __init__(self, nums):
#         self.pre = {num: num for num in nums}
#         self.rank = collections.defaultdict(lambda: 1)
#         self.cnt = collections.defaultdict(lambda: 1)
#
#     #找到最高级的父亲
#     def find(self, x):
#         while x != self.pre[x]:
#             x = self.pre[x]
#         return x
#     #合并两个结点
#     def merge(self, x, y):
#         if y not in self.pre:
#             return 1
#         root1, root2 = self.find(x), self.find(y)
#         print(root1,root2)
#         if root1 == root2:
#             return self.cnt[root1]
#         if self.rank[root1] < self.rank[root2]:
#             self.pre[root1] = root2
#             self.cnt[root2] += self.cnt[root1]
#             return self.cnt[root2]
#         elif self.rank[root1] > self.rank[root2]:
#             self.pre[root2] = root1
#             self.cnt[root1] += self.cnt[root2]
#             return self.cnt[root1]
#         else:
#             self.pre[root1] = root2
#             self.cnt[root2] += self.cnt[root1]
#             self.rank[root2] += 1
#             return self.cnt[root2]
#
# def longestConsecutive(nums):
#     dsu = DSU(nums)
#     res = 0
#     for num in nums:
#         res = max(res, dsu.merge(num, num + 1))
#
#     return res
#
# nums=[100,4,200,1,3,2,55]
# #print(longestConsecutive(nums))
#
# def isPalindrome(x):
#     if x<0 or (x%10 == 0 and x !=0):
#         return False
#
#     reversenum=0
#     while x>reversenum :
#         a=x%10
#         x=x//10
#         print(a)
#         reversenum = reversenum*10+a
#     print(reversenum)
#     return x == reversenum or x== reversenum//10
#
# #print(isPalindrome(11234))
# #print(isPalindrome(10))

##########################################################
#########################################################
#模式匹配
#注意逻辑分析
# class Solution:
#     def patternMatching(self, pattern,value):
#         count_a = sum(1 for ch in pattern if ch == 'a')
#         count_b = len(pattern) - count_a
#         #后续处理方便 count_a代表多的 count_b代表少的
#         if count_a < count_b:
#             count_a, count_b = count_b, count_a
#             pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)
#
#         if not value:#如果待匹配的字符串为空 那么要求parttern只能由一种字母
#             #count_b经处理 代表的是数量少的那个字母
#             return count_b == 0
#         if not pattern:
#             return False
#
#         #依次增加’a'分配的长度 例如2个'a' 字符串长12  那么每个'a'分配的就是从0-6个字符串
#         for len_a in range(len(value) // count_a + 1):
#             rest = len(value) - count_a * len_a
#             #如果没有‘b'那么就不能有rest  如果有'b’那么需要保证rest能被'b‘的数量整除
#             #因为次迭代都是以count_a间隔进行的 因此只要满足上述条件之一 每个'a’一定可以被分配0/1/2...个元素
#             if (count_b == 0 and rest == 0) or (count_b != 0 and rest % count_b == 0):
#                 #与'a‘间隔选择同理 保证每次递进每个'b’都可被分配
#                 len_b = 0 if count_b == 0 else rest // count_b
#                 pos, correct = 0, True
#                 value_a, value_b = None, None
#                 for ch in pattern:
#                     if ch == 'a':
#                         sub = value[pos:pos + len_a]
#                         #切分出一个'a‘对应的字符串
#                         if not value_a:#value_a还没被分配
#                             value_a = sub
#                         elif value_a != sub:#这种分配方式失败
#                             correct = False
#                             break
#                         pos += len_a
#                     else:
#                         sub = value[pos:pos + len_b]
#                         if not value_b:
#                             value_b = sub
#                         elif value_b != sub:
#                             correct = False
#                             break
#                         pos += len_b
#                 #分配正确且不是同一种分配
#                 if correct and value_a != value_b:
#                     return True
#
#         return False
#
# pattern = "abba"
# value = "dogcatcatdog"
#pattern = "abba"
#value = "dogcatcatfish"
######################################################################
#######################################################################
#1300 转变数组元素使其接近目标和
#双重二分查找枚举法
# class Solution:
#     def findBestValue(self, arr, target):
#         arr.sort()
#         n = len(arr)
#         prefix = [0]
#         for num in arr:
#             prefix.append(prefix[-1] + num)
#
#         l, r, ans = 0, max(arr), -1
#         while l <= r:
#             mid = (l + r) // 2
#             it = bisect.bisect_left(arr, mid)
#             cur = prefix[it] + (n - it) * mid
#             if cur <= target:
#                 ans = mid
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         #计算元素变化后数组和
#         def check(x):
#             return sum(x if num >= x else num for num in arr)
#
#         choose_small = check(ans)
#         choose_big = check(ans + 1)
#         return ans if abs(choose_small - target) <= abs(choose_big - target) else ans + 1

#################################################################################################
#################################################################################################
#二进制相加
#多看多想
#有空实现直接相加的方法
# class Solution:
#     def addBinary(self, a, b) -> str:
#         x, y = int(a, 2), int(b, 2)
#         while y:
#             print(bin(y)[2:])
#             print(bin(x)[2:])
#             print("###########")
#             answer = x ^ y
#             carry = (x & y) << 1
#             x, y = answer, carry
#         return bin(x)[2:]
#######################################
######################################
#数组相加
# class Solution(object):
#     def addToArrayForm(self, A, K):
#         """
#         :type A: List[int]
#         :type K: int
#         :rtype: List[int]
#         """
#
#


a = '10101'
b = '10101'



####################################################
####################################################
#16 最接近的三数之和
# class Solution(object):
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if len(nums)<3:
#             return 0
#
#         nums.sort()
#         ans = nums[0] + nums[1] + nums[2]
#         for i in range(len(nums)-2):
#             left = i+1
#             right = len(nums) - 1
#             while left <right:
#                 sum = nums[right] + nums[left] + nums[i]
#                 if abs(sum - target) < abs(ans-target):
#                     ans = sum
#
#                 if sum < target:
#                     left+=1
#                 elif sum >target:
#                     right-=1
#                 else:
#                     return ans
#         return ans

#########################################################
########################################################
#41缺失的第一个正数
# class Solution(object):
#     def firstMissingPositive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         for i in range(n):
#             if nums[i] < 0:
#                 nums[i] = n+1
#         for i in range(n):
#             num = abs(nums[i])
#             if num <= n:
#                 nums[num-1]= -abs(nums[num-1])
#
#         for i in range(n):
#             if nums[i] > 0:
#                 return i+1
#         return n+1

##############################################################
###############################################################
#209长度最小的子数组
# class Solution(object):
#     def minSubArrayLen(self, s, nums):
#         """
#         :type s: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#
#         n = len(nums)
#         ans = n + 1
#         start, end = 0, 0
#         total = 0
#         while end < n:
#             total += nums[end]
#             while total >= s:
#                 ans = min(ans, end - start + 1)
#                 total -= nums[start]
#                 start += 1
#             end += 1
#
#         return 0 if ans == n + 1 else ans

##############################################################
###############################################################
#215 数组中的第K个最大元素
class Solution(object):
    def maxheapfix(self,nums,index,size):
        l = index * 2 + 1
        r = index * 2 + 2
        maxindex = index
        if l < size and nums[l] > nums[maxindex]:
            maxindex = l
        if r < size and nums[r] > nums[maxindex]:
            maxindex = r
        if maxindex != index:
            nums[index],nums[maxindex] = nums[maxindex],nums[index]
            self.maxheapfix(nums,maxindex,size)

    def buildMaxHeap(self,nums,size):
        for  i in range(size//2,-1,-1):
            self.maxheapfix(nums,i,size)


    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = len(nums)
        self.buildMaxHeap(nums,size)
        for i in range(size-1,size-k,-1):
            nums[0],nums[i] = nums[i],nums[0]
            size = size -1
            self.maxheapfix(nums,0,size)

        return nums[0]




nums = [3,2,3,1,2,4,5,5,6]
solution = Solution()
ans = solution.findKthLargest(nums,4)
print(ans)