# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,r):
        if not root:
            return 
        self.inorder(root.left,r)
        r.append(root.val)
        self.inorder(root.right,r)    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        r1,r2,ans = deque(), deque(), []
        
        # Perform inorder traversal on both trees. This will give us 2 sorted list
        self.inorder(root1,r1)
        self.inorder(root2,r2)

        # Merge these 2 sorted lists
        while r1 and r2:
                if r1[0] < r2[0]:
                    ans.append(r1.popleft()) 
                else:
                    ans.append(r2.popleft())
                
        return ans+list(r1)+list(r2)