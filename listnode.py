'''
-*- coding: utf-8 -*-
@Author  : 李明洲
@Time    : 2020/6/26 9:39
@Software: PyCharm
@File    : listnode.py
'''

##############################################
#############################################
#移除重复节点
class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        existd = {head.val}
        pos = head
        while pos.next:
            cur = pos.next
            if cur.val not in existd:
                existd.add(cur.val)
                pos = pos.next
            else:
                pos.next = pos.next.next

        return head






head = [1, 1, 1, 1, 2]
solution = Solution()
print(solution.removeDuplicateNodes(head))