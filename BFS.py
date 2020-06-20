#-*- coding:utf-8 -*-
#Author:李明洲
#python 3.7.3
#@Time:2020/6/7 11:08

from collections import deque

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
#
# def level_order_tree(root, result):
#     if not root:
#         return
#     # 这里借助python的双向队列实现队列
#     # 避免使用list.pop(0)出站的时间复杂度为O(n)
#     queue = deque([root])
#
#     while queue:
#         node = queue.popleft()
#         # do somethings
#         result.append(node.val)
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#     return result
#
#
# if __name__ == "__main__":
#     tree = TreeNode(4)
#     tree.left = TreeNode(9)
#     tree.right = TreeNode(0)
#     tree.left.left = TreeNode(5)
#     tree.left.right = TreeNode(1)
#
#     print(level_order_tree(tree, []))
#     # [4, 9, 0, 5, 1]

from collections import deque

def bsf_graph(root):
    if not root:
        return
    # queue和seen为一对好基友，同时出现
    queue = deque([root])
    # seen避免图遍历过程中重复访问的情况，导致无法跳出循环
    seen = set([root])
    while queue:
        head = queue.popleft()
        # do somethings with the head node
        # 将head的邻居都添加进来
        for neighbor in head.neighbors:
            if neighbor not in seen:
                queue.append(neighbor)
                seen.add(neighbor)
    return xxx