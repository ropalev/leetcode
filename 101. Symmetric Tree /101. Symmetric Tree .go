package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func CheckReflection(tree1, tree2 *TreeNode) bool {
	if tree1 == nil && tree2 == nil {
		return true
	}
	if tree1 == nil || tree2 == nil {
		return false
	}
	if tree1.Val != tree2.Val {
		return false
	}
	return CheckReflection(tree1.Left, tree2.Right) && CheckReflection(tree1.Right, tree2.Left)
}

func isSymmetric(root *TreeNode) bool {
	return CheckReflection(root, root)
}

func main() {

}
