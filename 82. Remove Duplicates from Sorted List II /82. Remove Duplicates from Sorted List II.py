"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
"""


from typing import  Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def generateList(nums):
    start_node = None
    curr_node = None
    next_node = None
    for i in nums:
        if not start_node:
            start_node = ListNode(i, None)
            curr_node = start_node
            curr_node.next = next_node
            continue
        curr_node.next = ListNode(i, None)
        curr_node = curr_node.next

    return start_node
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first_seq = head
        curr_node = None
        end_seq = None
        while head.next:
            if not curr_node:
                curr_node = head.next
            if curr_node.val == first_seq.val:
                end_seq = curr_node
                continue
            else:
                first_seq.next = end_seq.next

if __name__ == "__main__":
    z = generateList([1,2,3,4,1,2])

