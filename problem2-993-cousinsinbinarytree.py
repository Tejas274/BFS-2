# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time Complexity : o(N)
#Space Complexity: o(h) -- stack space

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        if root == None:
            return False

        self.x_parent = None
        self.y_parent = None
        self.x_depth = 0
        self.y_depth = 0
        self.x = x
        self.y = y
        self.dfs_helper(root, None, 0)
        return (self.x_parent != self.y_parent) and (self.x_depth == self.y_depth)

    def dfs_helper(self, node: Optional[TreeNode], parent: Optional[TreeNode], depth: int) -> None:

        if node == None:
            return

        if node.val == self.x:
            self.x_parent = parent
            self.x_depth = depth

        if node.val == self.y:
            self.y_parent = parent
            self.y_depth = depth

        self.dfs_helper(node.left, node, depth + 1)
        self.dfs_helper(node.right, node, depth + 1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Time Complexity : o(n)
#Space Complexity: o(n) -- stack space
from queue import Queue


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        if root == None:
            return False

        q = Queue()
        q.put(root)
        x_found = False
        y_found = False

        while not q.empty():
            size = q.qsize()
            for i in range(size):
                curr = q.get()

                if curr.val == x:
                    x_found = True

                if curr.val == y:
                    y_found = True

                if curr.left != None and curr.right != None:
                    if curr.left.val == x and curr.right.val == y:
                        return False
                    if curr.left.val == y and curr.right.val == x:
                        return False

                if curr.left != None:
                    q.put(curr.left)

                if curr.right != None:
                    q.put(curr.right)

            if x_found == True and y_found == True:
                return True

            if x_found == True or y_found == True:
                return False

        return False


















