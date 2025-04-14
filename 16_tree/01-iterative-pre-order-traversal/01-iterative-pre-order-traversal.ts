import { TreeNode } from '../../TypeScriptDataStructure/BinaryTree/TreeNode'

const iterative_pre_traversal = (root: TreeNode) => {
  const st = []
  const res = []
  while (st.length > 0 || root != null) {
    if (root != null) {
      st.push(root)
      res.push(root.val)
      root = root.left
    }
    else {
      root = st.pop()
      root = root.right
    }
  }
  return res
}

const root = new TreeNode(10, new TreeNode(20,null, new TreeNode(40)), new TreeNode(30))
console.log(iterative_pre_traversal(root))