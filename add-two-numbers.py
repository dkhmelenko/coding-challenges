"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def add_two_numbers(self, l1, l2):
        num1 = self.readNumber(l1)
        num2 = self.readNumber(l2)
        sum = str(int(num1) + int(num2))
        res = self.makeNumber(sum)
        return res


    def read_number(self, input_list):
        num = ""
        while input_list != None:
            num += (str(input_list.val))
            input_list = input_list.next

        print(num[::-1])
        return num[::-1]


    def make_number(self, number):
        num = number[::-1]
        print(num)
        ret_list = ListNode(num[0])
        head = ret_list
        for i in num[1:]:
            head.next = ListNode(i)
            head = head.next
        print(head)
        return ret_list
