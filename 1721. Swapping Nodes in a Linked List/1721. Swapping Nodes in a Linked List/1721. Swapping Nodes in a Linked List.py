# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from utils.ListNode import LinkedList, ListNode


class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return []
        length = 0
        temp = head
        while temp:
            length += 1
            if length == k:
                val1 = temp.val
            temp = temp.next
        mid = length - k + 1
        length = 0
        temp = head
        while temp:
            length += 1
            if length == mid:
                val2 = temp.val
                temp.val = val1
                break
            temp = temp.next
        length = 0
        temp = head
        while temp:
            length += 1
            if length == k:
                temp.val = val2
                break
            temp = temp.next
        return head


if __name__ == "__main__":
    l1 = LinkedList().from_list([1, 2, 3, 4, 5])
    Solution().swapNodes(l1.head, 2)
    l1.print_list()
