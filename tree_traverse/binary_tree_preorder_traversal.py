from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


def test_solution():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    assert Solution().preorderTraversal(root) == [1, 2, 3]
    assert Solution().preorderTraversal(None) == []
    root = TreeNode(1)
    assert Solution().preorderTraversal(root) == [1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    assert Solution().preorderTraversal(root) == [1, 2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    assert Solution().preorderTraversal(root) == [1, 2]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert Solution().preorderTraversal(root) == [1, 2, 3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert Solution().preorderTraversal(root) == [1, 2, 3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert Solution().preorderTraversal(root) == [1, 2, 3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    assert Solution().preorderTraversal(root) == [1, 2, 3, 4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    assert Solution().preorderTraversal(root) == [1, 2, 3, 4]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    assert Solution().preorderTraversal(root) == [1, 2, 3, 4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    assert Solution().preorderTraversal(root) == [1, 2, 3, 4, 5]


if __name__ == '__main__':
    test_solution()
    print("All tests have passed successfully.")
