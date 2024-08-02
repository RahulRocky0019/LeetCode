# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Approach 1
        # temp = node
        # while temp:
        #     temp.val = temp.next.val
        #     if temp.next.next is None:
        #         temp.next = None
        #         break
        #     temp = temp.next

        # Approach 2
        node.val = node.next.val
        node.next = node.next.next
