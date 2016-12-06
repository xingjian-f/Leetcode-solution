# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def dfs(self, node, val, cnt, ret):
        node_id = cnt[0]
        cnt[0] += 1
        val[node_id] = node.val
        if node.left is not None:
            left = self.dfs(node.left, val, cnt, ret)
        else:
            left = -1
        if node.right is not None:
            right = self.dfs(node.right, val, cnt, ret)
        else:
            right = -1
        ret.append((node_id,left,right))
        return node_id


    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        tree = []
        val = {}
        cnt = [0]
        self.dfs(root, val, cnt, tree)
        tree = ','.join(map(lambda x:'%d,%d,%d'%x, tree))
        val = ','.join(map(lambda x:'%d,%d'%x, val.items()))
        return '#'.join([tree, val])


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        print data
        data = data.split('#')
        tree = map(int, data[0].split(','))
        vals = map(int, data[1].split(','))
        rec = {}
        for i in range(0,len(tree),3):
            node_id = tree[i]
            left_id = tree[i+1]
            right_id = tree[i+2]
            if node_id not in rec:
                rec[node_id] = TreeNode(None)
            node = rec[node_id]
            if left_id != -1:
                if left_id not in rec:
                    rec[left_id] = TreeNode(None)
                node.left = rec[left_id]
            if right_id != -1:
                if right_id not in rec:
                    rec[right_id] = TreeNode(None)
                node.right = rec[right_id]
        for i in range(0, len(vals), 2):
            node_id = vals[i]
            val = vals[i+1]
            node = rec[node_id]
            node.val = val 

        return rec[0]
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))