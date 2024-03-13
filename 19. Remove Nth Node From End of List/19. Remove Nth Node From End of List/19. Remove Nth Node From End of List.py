# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from utils.ListNode import LinkedList, ListNode


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return []
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        start = head
        end = None
        mid = length - n + 1
        length = 1
        if mid == 1:
            head = head.next
            return head if head else None
        temp = head
        while temp:
            if length == mid - 1:
                start = temp
            if length == mid + 1:
                end = temp
            length += 1
            temp = temp.next
        start.next = end
        return head


if __name__ == "__main__":
    s = Solution()
    d = LinkedList().from_list([1, 2])
    s.removeNthFromEnd(d.head, 2)
    d.print_list()
