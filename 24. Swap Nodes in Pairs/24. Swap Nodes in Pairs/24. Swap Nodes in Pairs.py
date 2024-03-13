# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from utils.ListNode import LinkedList, ListNode


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        temp1 = head
        temp2 = head.next
        while temp1 and temp2:
            prev.next = temp2
            temp1.next = temp2.next
            temp2.next = temp1

            prev = temp1
            temp1 = temp1.next
            if temp1:
                temp2 = temp1.next

        return dummy.next




if __name__ == "__main__":
    c = Solution()
    l1 = LinkedList().from_list([1, 2, 3, 4, 5, 6])
    z = c.swapPairs(l1.head)
    l1.head = z
    l1.print_list()