from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        answer = []
        def form_answer(node: Optional[TreeNode], level: int):
            if not node:
                return
            if len(answer) == level:
                answer.append([])
            answer[level].append(node.val)

            form_answer(node.left, level + 1)
            form_answer(node.right, level + 1)

        form_answer(root, 0)
        return answer

def test_solution():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().levelOrder(root) == [[3], [9, 20], [15, 7]]
    assert Solution().levelOrder(None) == []
    root = TreeNode(1)
    assert Solution().levelOrder(root) == [[1]]
    root = TreeNode(1)
    root.left = TreeNode(2)
    assert Solution().levelOrder(root) == [[1], [2]]
    root = TreeNode(1)
    root.right = TreeNode(2)
    assert Solution().levelOrder(root) == [[1], [2]]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert Solution().levelOrder(root) == [[1], [2, 3]]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert Solution().levelOrder(root) == [[1], [2], [3]]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert Solution().levelOrder(root) == [[1], [2], [3]]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    assert Solution().levelOrder(root) == [[1], [2, 3], [4]]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    assert Solution().levelOrder(root) == [[1], [2], [3, 4]]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    assert Solution().levelOrder(root) == [[1], [2], [3, 4]]

if __name__ == '__main__':
    test_solution()
    print("All tests passed")
