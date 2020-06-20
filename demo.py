#-*- coding:utf-8 -*-
#Author:李明洲
#python 3.7.3
#@Time:2020/6/11 11:04

import collections
# def dailyTemperatures(T):
#     lenT=len(T)
#     ans=[]
#     for i in range(0,lenT):
#         ans.append(0)
#         for j in range(i+1,lenT):
#             if T[j] > T[i]:
#                 ans[-1] = j -i
#                 break
#     return ans
#
# temperatures = [89,62,70,58,47,47,46,76,100,70]
#
# def dailyTemperatures(T):
#     length = len(T)
#     stack = []
#     ans = [0]*length
#     for i in range(length):
#         tem=T[i]
#         while stack and tem > T[stack[-1]]:
#             prev_index = stack.pop()
#             ans[prev_index] = i - prev_index
#         stack.append(i)
#         print(stack)
#     return ans
# print(dailyTemperatures(temperatures))

# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
# 数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，
# 这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
#

# 输入: [1,2,1]
# 输出: [2,-1,2]
# 解释: 第一个 1 的下一个更大的数是 2；
# 数字 2 找不到下一个更大的数；
# 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
def nextMax(T):
    len1=len(T)
    T.extend(T[:-1])
    length = len(T)
    stack = []
    ans = [0]*length
    for i in range(length):
        tem=T[i]
        while stack and tem > T[stack[-1]]:
            prev_index = stack.pop()
            ans[prev_index] = tem
        stack.append(i)
    return ans[:len1]



# def find132pattern(nums):
#     length = len(nums)
#     if length < 3:
#         return False
#
#     stack = []
#     minnum=[0]*length
#     minnum[0] = nums[0]
#     for i in range(1,length):
#         minnum[i] = min(minnum[i-1],nums[i])
#
#     for i in range(length-1,-1,-1):
#         if nums[i] > minnum[i]:
#             while stack and stack[-1] <= minnum[i]:
#                 stack.pop()
#             if stack and stack[-1] < nums[i]:
#                 return True
#             stack.append(nums[i])
#     return False
#
# num = [2,3,1,2]
# print(find132pattern(num))

# hours = [9,9,6,0,6,6,9]
# def longestWPI(hours) -> int:
#     n = len(hours)
#
#     score = [0] * n
#     for i in range(n):
#         if hours[i] > 8:
#             score[i] = 1
#         else:
#             score[i] = -1
#
#     # 前缀和
#     presum = [0] * (n + 1)
#     for i in range(1, n + 1):
#         presum[i] = presum[i - 1] + score[i - 1]
#
#     stack = []
#     # 顺序生成单调栈，栈中元素从第一个元素开始严格单调递减，最后一个元素肯定是数组中的最小元素所在位置
#     for i in range(n + 1):
#         if not stack or presum[stack[-1]] > presum[i]:
#             stack.append(i)
#
#     # 倒序扫描数组，求最大长度坡
#     i = n
#     ans = 0
#     while i > ans:
#         while stack and presum[stack[-1]] < presum[i]:
#             ans = max(ans, i - stack[-1])
#             stack.pop()
#         i -= 1
#     return ans
# print(longestWPI(hours))

# def buildArray(target, n):
#     oplist = []
#     nownum=1
#     for i in target:
#         while i > nownum:
#             oplist.append('push')
#             oplist.append('pop')
#             nownum = nownum + 1
#         if i == nownum:
#             oplist.append('push')
#             nownum = nownum + 1
#     return oplist
#
# print(buildArray([1,2,3],3))

asteroid = [1,-2,-2,-2]
def collese(a,b):
    return a<0 and b>0

def asteroidCollision(asteroids):
    stack=[]

    for aster in asteroids:
        if not stack or  not collese(aster,stack[-1]):
            stack.append(aster)
        while stack and collese(aster,stack[-1]):
            if abs(aster) >  abs(stack[-1]):
                stack.pop()
                if not stack or not collese(aster,stack[-1]):
                    stack.append(aster)
            elif abs(aster) == abs(stack[-1]):
                stack.pop()
                flag = True
                break
            else:
                break
    return stack

#print(asteroidCollision(asteroid))

# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
# def canCompleteCircuit(gas, cost):
#     n = len(gas)
#     total_tank, curr_tank = 0, 0
#     starting_station = 0
#     for i in range(n):
#         total_tank += gas[i] - cost[i]
#         curr_tank += gas[i] - cost[i]
#         if curr_tank < 0:
#             starting_station = i + 1
#             curr_tank = 0
#     return starting_station if total_tank >= 0 else -1
# print(canCompleteCircuit(gas,cost))

# def wiggleMaxLength(nums):
#     length = len(nums)
#     if length < 3:
#         return length
#
#     up,down =1,1
#     for i in range(1,length):
#         if nums[i] >= nums[i-1]:
#             up = down +1
#         elif nums[i] < nums[i-1]:
#             down = up + 1
#     return max(up,down)
# nums = [1,7,4,9,2,5]
# print(wiggleMaxLength(nums))

# def reconstructQueue(people):
#     people.sort(key = lambda x:(-x[0],x[1]))
#     output = []
#     for i,j in people:
#         output.insert(j,[i,j])
#     return output
#
# people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# print(reconstructQueue(people))

nums = [-1, 0, 1, 2, -1,-1,1, -4]
# def threeSum(nums):
#     n = len(nums)
#     nums.sort()
#     ans = list()
#
#     # 枚举 a
#     for first in range(n-2):
#         # 需要和上一次枚举的数不相同
#         if first > 0 and nums[first] == nums[first - 1]:
#             continue
#         # c 对应的指针初始指向数组的最右端
#         third = n - 1
#         target = -nums[first]
#         # 枚举 b
#         for second in range(first + 1, n):
#             # 需要和上一次枚举的数不相同
#             if second > first + 1 and nums[second] == nums[second - 1]:
#                 continue
#             # 需要保证 b 的指针在 c 的指针的左侧
#             while second < third and nums[second] + nums[third] > target:
#                 third -= 1
#             # 如果指针重合，随着 b 后续的增加
#             # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
#             if second == third:
#                 break
#             if nums[second] + nums[third] == target:
#                 ans.append([nums[first], nums[second], nums[third]])
#
#     return ans
# print(threeSum(nums))

# prices = [1,3, 2, 8, 4, 9]
# fee = 2
# def maxProfit(prices, fee):

#
# class Solution:
#     def findBestValue(self, arr, target):
#         arr_sum = sum(arr)
#         if arr_sum <= target:
#             return max(arr)
#         arr.sort()
#         prefix = [0]
#         for num in arr:
#             prefix.append(prefix[-1] + num)
#         aver = arr_sum // len(arr)
#


# class Solution:
#     def search(self, nums, target):
#         if not nums:
#             return -1
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] == target:
#                 return mid
#             if nums[0] <= nums[mid]:
#                 if nums[0] <= target < nums[mid]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#             else:
#                 if nums[mid] < target <= nums[len(nums) - 1]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#         return -1


# target = 0
# solution = Solution()
# print(solution.reverseBetween(arr))



