class Codec:
    def serialize(self, root):
        def helper(node):
            if not node:
                serialized.append("#")
                return
            serialized.append(node.val)
            helper(node.left)
            helper(node.right)
          
        serialized = []        
        helper(root)
        return ",".join([str(n) for n in serialized])

    def deserialize(self, data):
        def helper(queue):
            if not queue:
                return None
            node_val = queue.popleft()            
            if node_val == "#":
                return None
            
            node = TreeNode(node_val)
            node.left = helper(q)
            node.right = helper(q)
            return node
        
        q = deque()
        for n in data.split(","):
            q.append(n)
        return helper(q)