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
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinatryTree(newNode)
        else:
            t = BinatryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinatryTree(newNode)
        else:
            t = BinatryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRootVal(self):
        return self.key

    def setRootVal(self,obj):
        self.key = obj

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild
    #前序
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
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














