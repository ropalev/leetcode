# Definition for singly-linked list.
from utils.ListNode import LinkedList, ListNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp1 = l1
        temp2 = l2
        num1 = []
        num2 = []
        while temp1:
            num1.append(temp1.val)
            temp1 = temp1.next
        while temp2:
            num2.append(temp2.val)
            temp2 = temp2.next
        num1.reverse()
        num2.reverse()
        num1 = int(''.join([str(i) for i in num1]))
        num2 = int(''.join([str(i) for i in num2]))
        num = num1 + num2
        res = list(map(int, str(num)))
        res.reverse()
        if res:
            head = ListNode(res[0])
            temp = head
            for i in range(1, len(res)):
                temp.next = ListNode(res[i])
                temp = temp.next

        return head


if __name__ == '__main__':
    l1 = LinkedList().from_list([0,1])
    l2 = LinkedList().from_list([1,2,3,4,5])
    s = Solution()
    r = s.addTwoNumbers(l1.head, l2.head)
    while r:
        print(r.val)
        r = r.next



