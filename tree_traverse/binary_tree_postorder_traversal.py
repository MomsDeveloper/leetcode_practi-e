from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

def test_solution():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    assert Solution().postorderTraversal(root) == [3, 2, 1]
    assert Solution().postorderTraversal(None) == []
    root = TreeNode(1)
    assert Solution().postorderTraversal(root) == [1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    assert Solution().postorderTraversal(root) == [2, 1]
    root = TreeNode(1)
    root.right = TreeNode(2)
    assert Solution().postorderTraversal(root) == [2, 1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert Solution().postorderTraversal(root) == [2, 3, 1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert Solution().postorderTraversal(root) == [3, 2, 1]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert Solution().postorderTraversal(root) == [3, 2, 1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    assert Solution().postorderTraversal(root) == [2, 4, 3, 1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    assert Solution().postorderTraversal(root) == [3, 4, 2, 1]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    assert Solution().postorderTraversal(root) == [3, 4, 2, 1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    assert Solution().postorderTraversal(root) == [2, 4, 5, 3, 1]

if __name__ == '__main__':
    test_solution()
    print("All tests passed")