#10. 正则表达式匹配
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
#使用动态规划的方法
#核心是状态转移方程的求解
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         m, n = len(s), len(p)
#
#         def matches(i: int, j: int) -> bool:
#             if i == 0:
#                 return False
#             if p[j - 1] == '.':
#                 return True
#             return s[i - 1] == p[j - 1]
#
#         f = [[False] * (n + 1) for _ in range(m + 1)]
#         f[0][0] = True
#         for i in range(m + 1):
#             for j in range(1, n + 1):
#                 if p[j - 1] == '*':
#                     f[i][j] |= f[i][j - 2]
#                     if matches(i, j - 1):
#                         f[i][j] |= f[i - 1][j]
#                 else:
#                     if matches(i, j):
#                         f[i][j] |= f[i - 1][j - 1]
#         return f[m][n]
#########################################################################
#########################################################################
#44 通配符匹配
# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
#
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。

# class Solution:
#     def isMatch(self, s, p):
#         s_len = len(s)
#         p_len = len(p)
#
#         # base cases
#         if p == s or p == '*':
#             return True
#         if p == '' or s == '':
#             return False
#
#         # init all matrix except [0][0] element as False
#         d = [[False] * (s_len + 1) for _ in range(p_len + 1)]
#         d[0][0] = True
#
#         # DP compute
#         for p_idx in range(1, p_len + 1):
#             # the current character in the pattern is '*'
#             if p[p_idx - 1] == '*':
#                 s_idx = 1
#                 # d[p_idx - 1][s_idx - 1] is a string-pattern match
#                 # on the previous step, i.e. one character before.
#                 # Find the first idx in string with the previous math.
#                 while not d[p_idx - 1][s_idx - 1] and s_idx < s_len + 1:
#                     s_idx += 1
#                 # If (string) matches (pattern),
#                 # when (string) matches (pattern)* as well
#                 d[p_idx][s_idx - 1] = d[p_idx - 1][s_idx - 1]
#                 # If (string) matches (pattern),
#                 # when (string)(whatever_characters) matches (pattern)* as well
#                 while s_idx < s_len + 1:
#                     d[p_idx][s_idx] = True
#                     s_idx += 1
#             # the current character in the pattern is '?'
#             elif p[p_idx - 1] == '?':
#                 for s_idx in range(1, s_len + 1):
#                     d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1]
#                     # the current character in the pattern is not '*' or '?'
#             else:
#                 for s_idx in range(1, s_len + 1):
#                     # Match is possible if there is a previous match
#                     # and current characters are the same
#                     d[p_idx][s_idx] = \
#                         d[p_idx - 1][s_idx - 1] and p[p_idx - 1] == s[s_idx - 1]
#
#         return d[p_len][s_len]
#######################################################################################
######################################################################################
#322找零钱
# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         dp = [float('inf')] * (amount + 1)
#         dp[0] = 0
#
#         for coin in coins:
#             for x in range(coin, amount + 1):
#                 dp[x] = min(dp[x], dp[x - coin] + 1)
#         print(dp)
#         return dp[amount] if dp[amount] != float('inf') else -1

######################################################################
#####################################################################
#按摩师
# class Solution(object):
#     def massage(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         length = len(nums)
#         dp =[0]*(length+1)
#         dp[1] = nums[0]
#         for i in range(2,length+1):
#             dp[i] = max(dp[i-2]+nums[i-1],dp[i-1])
#         return dp[-1]

########################################################################
#########################################################################
#139 单词拆分
# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#         dp = [False] * (len(s) + 1)
#         dp[0] = True
#         for i in range(len(s)):
#             if dp[i] == True:
#                 for j in range(i+1,len(s)+1):
#                     if s[i:j]  in wordDict:
#                         dp[j] = True
#         return dp[-1]

###########################################################################
##########################################################################     ??????????????????????????????????????????
#140 单词拆分                                                                    ????????????????????????????????????????
from typing import List
from collections import deque
# class Solution:
#     def wordBreak(self, s, wordDict):
#         dp = [False] * (len(s) + 1)
#         dp[0] = True
#         for i in range(len(s)):
#             if dp[i] == True:
#                 for j in range(i+1,len(s)+1):
#                     if s[i:j]  in wordDict:
#                         dp[j] = True
#
#         ans = []
#         res = []
#         def search(s):
#             for j in range(len(s)+1,-1,-1):
#

###########################################################################
##########################################################################
# #32最长有效括号
# class Solution(object):
#     def longestValidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         maxans = 0
#         n = len(s)
#         dp = [0] * (n + 1)
#         for i in range(1,n):
#             index = i + 1
#             if s[i] == ')':
#                 if s[i-1] == '(':
#                     dp[index] = dp[index-2] + 2
#                 elif i - dp[index-1] > 0 and s[i - dp[index-1] - 1] == '(':
#                     dp[index] = dp[index-1] + dp[index - dp[index-1] -2] +2
#             maxans = max(maxans,dp[index])
#
#         return maxans

###########################################################################
##########################################################################
#一些简单的练手
class Solution(object):
    def numMatchingSubseq(self, S, words):
        ans = 0
        heads = [[] for _ in range(26)]
        for word in words:
            it = iter(word)
            heads[ord(next(it)) - ord('a')].append(it)
        for letter in S:
            letter_index = ord(letter) - ord('a')
            old_bucket = heads[letter_index]
            heads[letter_index] = []

            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)  #没有下一个元素时返回None
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)
                else:
                    ans += 1

        return ans

solution = Solution()
S = "abcde"
words = ["a", "bb", "acd", "ace"]
print(solution.numMatchingSubseq(S,words))