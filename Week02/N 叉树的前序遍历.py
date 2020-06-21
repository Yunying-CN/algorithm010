class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        s = [root]
        res = []
        while s:
            node = s.pop()
            res.append(node.val)
            s.extend(node.children[::-1])
        return res