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

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {

	//Edge case
	if list1 == nil {
		return list2
	} else if list2 == nil {
		return list1
	}
	if list1.Val > list2.Val {
		temp := list2
		list2 = list1
		list1 = temp
	}
	result := list1
	prevNode := list1
	for list2 != nil {
		for list1 != nil && list1.Val <= list2.Val {
			prevNode = list1
			list1 = list1.Next
		}
		if list1 == nil {
			prevNode.Next = list2
			break
		}
		prevNode.Next = list2
		list2 = list2.Next
		prevNode.Next.Next = list1
		prevNode = prevNode.Next
	}
	return result
}

func main() {
	list1 := &ListNode{
		Val: 4,
		Next: &ListNode{
			Val: 5,
			Next: &ListNode{
				Val:  10,
				Next: nil,
			},
		},
	}
	list2 := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 4,
			Next: &ListNode{
				Val:  9,
				Next: nil,
			},
		},
	}
	mergeTwoLists(list1, list2)
}
