export class TreeNode {
  val: number
  left: TreeNode
  right: TreeNode

  constructor(val: number, left: TreeNode = null, right: TreeNode = null) {
    this.val = val
    this.left = left
    this.right = right
  }
}
