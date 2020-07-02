'''
-*- coding: utf-8 -*-
@Author  : 李明洲
@Time    : 2020/6/30 10:53
@Software: PyCharm
@File    : heap.py
'''
import collections
import heapq
##############################################################
###############################################################
#215 数组中的第K个最大元素
# class Solution(object):
#     def maxheapfix(self,nums,index,size):
#         l = index * 2 + 1
#         r = index * 2 + 2
#         maxindex = index
#         if l < size and nums[l] > nums[maxindex]:
#             maxindex = l
#         if r < size and nums[r] > nums[maxindex]:
#             maxindex = r
#         if maxindex != index:
#             nums[index],nums[maxindex] = nums[maxindex],nums[index]
#             self.maxheapfix(nums,maxindex,size)
#
#     def buildMaxHeap(self,nums,size):
#         for  i in range(size//2,-1,-1):
#             self.maxheapfix(nums,i,size)
#
#
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         size = len(nums)
#         self.buildMaxHeap(nums,size)
#         for i in range(size-1,size-k,-1):
#             nums[0],nums[i] = nums[i],nums[0]
#             size = size -1
#             self.maxheapfix(nums,0,size)
#
#         return nums[0]

##############################################################
###############################################################
# 数组中的个最小的k个元素
# class Solution(object):
#     def minheapfix(self,arr, index, size):
#         l = index * 2 + 1
#         r = index * 2 + 2
#         minindex = index
#         if l < size and arr[l] < arr[minindex]:
#             minindex = l
#         if r < size and arr[r] < arr[minindex]:
#             minindex = r
#         if minindex != index:
#             arr[minindex], arr[index] = arr[index], arr[minindex]
#             self.minheapfix(arr, minindex, size)
#
#     def getLeastNumbers(self, arr, k):
#         """
#         :type arr: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         minKlist = []
#         size = len(arr)
#         for i in range(size // 2, -1, -1):
#             self.minheapfix(arr, i, size)
#         for i in range(size - 1, size - k-1, -1):
#             print('a')
#             minKlist.append(arr[0])
#             arr[0], arr[i] = arr[i], arr[0]
#             size = size - 1
#             self.minheapfix(arr, 0, size)
#         return minKlist

##############################################################
###############################################################
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         # 大顶堆
#         countFrequency = collections.defaultdict(int)
#         for i in s:
#             countFrequency[i] += 1
#         lst = []
#         heapq.heapify(lst)
#
#         for i in countFrequency:
#             for j in range(countFrequency[i]):
#                 heapq.heappush(lst, (-countFrequency[i], i))
#         return ''.join([heapq.heappop(lst)[1] for _ in range(len(s))])

############################################################################
#############################################################################
# 378 有序矩阵中第K小的元素
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        uplist = []
        R,C = len(matrix),len(matrix[0])
        for i in range(R):
            for j in range(C):
                uplist.append(matrix[i][j])
        heapq.heapify(uplist)
        for i in range(k-1):
            heapq.heappop(uplist)
        return uplist[0]


nums = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 3
solution = Solution()
ans = solution.kthSmallest(nums, k)
print(ans)


# def stringToString(input):
#     return input
#
#
# def main():
#     import sys
#     import io
#     def readlines():
#         for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
#             yield line.strip('\n')
#
#     lines = readlines()
#     while True:
#         try:
#             line = next(lines)
#             s = stringToString(line)
#
#             ret = Solution().frequencySort(s)
#
#             out = (ret)
#             print(out)
#         except StopIteration:
#             break
#
# if __name__ == '__main__':
#     main()