from collections import deque

class Codec:

    def serialize(self, root):
        if not root:
            return ""

        q = deque([root])
        code = ""

        while q:
            a = q.popleft()

            if a:
                code += str(a.val) + ","
                q.append(a.left)
                q.append(a.right)
            else:
                code += "null,"

        return code[:-1]


    def deserialize(self, code):
        if not code:
            return None

        arr = code.split(",")
        tree = deque()

        for i in arr:
            if i == "null":
                tree.append(None)
            else:
                tree.append(TreeNode(int(i)))

        root = tree.popleft()
        q = deque([root])

        while tree and q:
            node = q.popleft()

            if node:
                node.left = tree.popleft()
                q.append(node.left)

                if tree:
                    node.right = tree.popleft()
                    q.append(node.right)

        return root