'''
-*- coding: utf-8 -*-
@Author  : 李明洲
@Time    : 2020/6/21 8:51
@Software: PyCharm
@File    : BTree.py
'''
#二叉树的链表实现
class BinatryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.left = None
        self.right = None

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinatryTree(newNode)
        else:
            t = BinatryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinatryTree(newNode)
        else:
            t = BinatryTree(newNode)
            t.right = self.right
            self.right = t

    def val(self):
        return self.key

    def setRootVal(self,obj):
        self.key = obj

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right
    #前序
    def preorder(self):
        print(self.key)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
#前序
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
#后序
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())
#中序
def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())
#层序遍历
def PrintFromTopToBottom(root):
    ans = []
    if root == None:
        return ans
    else:
        q = [root]
        while q:
            node = q.pop(0)
            ans.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans

#层序遍历恢复
def createtree(l):
    if l[0]:
        root = BinatryTree(l[0])
        nodes = [root]
        id = 1
        while nodes and id < len(l):
            node = nodes[0]  # 依次为每个节点分配子节点
            node.left = BinatryTree(l[id]) if l[id] else None
            nodes.append(node.left)
            node.right = BinatryTree(l[id + 1]) if id < len(l) - 1 and l[id + 1] else None
            nodes.append(node.right)
            id += 2  # 每次取出两个节点
            nodes.pop(0)
        return root
    else:
        return None


#######################################################
#######################################################
#124 二叉树的最大路径和
#递归的方法
# class Solution(object):
#     def __init__(self):
#         self.maxSum = float("-inf")
#
#     def maxPathSum(self,root):
#         def dfs(root):
#             if not root :
#                 return 0
#             leftmax = max(0,dfs(root.left))
#             rightmax = max(0,dfs(root.right))
#
#             priceNewpath = root.val() + leftmax + rightmax
#
#             self.maxSum = max(self.maxSum,priceNewpath)
#             return root.val() + max(leftmax,rightmax)
#
#         dfs(root)
#         return self.maxSum
# solution = Solution()
# input = [1,2,3]
# root = createtree(input)
# # root = BinatryTree(-10)
# # root.insertLeft(9)
# # root.insertRight(20)
# # root.right.insertLeft(15)
# # root.right.insertRight(7)
# print(solution.maxPathSum(root))

###########################################
##########################################
#1028 先序遍历还原二叉树
#使用栈来保存遍历路径 根据深度插入节点
class Solution:
    def recoverFromPreorder(self, S):
        path, pos = list(), 0
        while pos < len(S):
            level = 0
            while S[pos] == '-':
                level += 1
                pos += 1
            value = 0
            while pos < len(S) and S[pos].isdigit():
                value = value * 10 + (ord(S[pos]) - ord('0'))
                pos += 1
            node = BinatryTree(value)
            if level == len(path):
                if path:
                    path[-1].left = node
            else:
                path = path[:level]
                path[-1].right = node
            path.append(node)
        return path[0]

tree = "1-2--3---4-5--6---7"
root = "1"
solution = Solution()
print(solution.recoverFromPreorder(root).val())





