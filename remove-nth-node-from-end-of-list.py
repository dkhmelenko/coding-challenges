"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lenth = self.get_head_len(head)
        print(lenth)

        to_remove = lenth - n

        curr = head
        prev = curr
        counter = 0
        while curr is not None:
            print(curr)
            if counter == to_remove:
                # if we need to remove the first node,
                # then shift the pointer
                if prev == curr:
                    head = head.next
                else:
                    prev.next = curr.next
                break
            counter += 1
            prev = curr
            curr = curr.next

        return head

    def get_head_len(self, head):
        lenth = 0
        curr = head
        while curr != None:
            curr = curr.next
            lenth += 1
        return lenth