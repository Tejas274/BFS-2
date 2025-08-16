# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Time Complexity : o(n)
#Space Complexity : o(n)
#using bfs
from queue import Queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
            return []
        result = []
        q = Queue()
        q.put(root)

        while not q.empty():
            queuesize = q.qsize()
            for i in range(queuesize):
                item = q.get()
                if i == queuesize - 1:
                    result.append(item.val)

                if item.left != None:
                    q.put(item.left)

                if item.right != None:
                    q.put(item.right)

        return result


#Time Complexity : o(n)
#Space Complexity : o(h)
from queue import Queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
           return []
        self.result = []

        self.helper(root, 0)

        return self.result


    def helper(self, root: Optional[TreeNode], counter: int) -> None:

        if root == None:
           return

        if len(self.result) ==  counter:
           self.result.append(root.val)
        else:
           self.result[counter] = root.val

        self.helper(root.left, counter + 1)
        self.helper(root.right, counter + 1)