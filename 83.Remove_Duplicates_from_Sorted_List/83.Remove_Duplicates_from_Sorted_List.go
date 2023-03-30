/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	var p1, p2 *ListNode
	if head == nil {
		return head
	}
	p1 = head
	p2 = head.Next

	for p1.Next != nil {
		if p2 == nil {
			p1.Next = nil
			break
		}
		if p1.Val == p2.Val {
			p2 = p2.Next
		} else {
			p1.Next = p2
			p1 = p2
			p2 = p1.Next
		}
	}
	return head
}

func main() {
	list1 := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 1,
			Next: &ListNode{
				Val: 2,
				Next: &ListNode{
					Val: 2,
					Next: &ListNode{
						Val: 3,
						Next: &ListNode{
							Val:  3,
							Next: nil,
						},
					},
				},
			},
		},
	}
	deleteDuplicates(list1)
}
