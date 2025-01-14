import collections

'''
This solution uses Breadth-First Search Algorithm
'''

#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

class Solution_1:
    def rightSideView(self, root):

        #Define results | use deque instead of list as O(1) instead of O(n)
        res=[]
        queue=collections.deque()

        # add 1st node to queue
        queue.append(root)

        # intialise while in queue is not empty
        while queue:
            queue_len=len(queue)
            level= []
            
            # iterating over length at  each level
            for _ in range(queue_len):
                #deqeues node value
                node = queue.popleft()
                # checks if node is empty value.
                if node:
                    #Adds node value to level for _ in range(queue_len)
                    level.append(node.val)
                    # left born & right born of node append to queue
                    queue.append(node.left)
                    queue.append(node.right)
            #Appends right most reading.
            if level:
                res.append(level[-1])

        return res