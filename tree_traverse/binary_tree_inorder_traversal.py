from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


def test_solution():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    assert Solution().inorderTraversal(root) == [1, 3, 2]
    assert Solution().inorderTraversal(None) == []
    root = TreeNode(1)
    assert Solution().inorderTraversal(root) == [1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    assert Solution().inorderTraversal(root) == [2, 1]
    root = TreeNode(1)
    root.right = TreeNode(2)
    assert Solution().inorderTraversal(root) == [1, 2]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert Solution().inorderTraversal(root) == [2, 1, 3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert Solution().inorderTraversal(root) == [3, 2, 1]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert Solution().inorderTraversal(root) == [1, 2, 3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    assert Solution().inorderTraversal(root) == [2, 1, 4, 3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    assert Solution().inorderTraversal(root) == [3, 2, 4, 1]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    assert Solution().inorderTraversal(root) == [1, 3, 2, 4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert Solution().inorderTraversal(root) == [4, 2, 5, 1, 6, 3, 7]


if __name__ == "__main__":
    test_solution()
    print("All tests passed")
