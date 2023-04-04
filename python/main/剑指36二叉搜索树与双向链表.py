class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeToDoublyList(root: Node) -> Node:
    if root == None:
        return None

    head = pre = None

    def _in_order(cur: Node):
        nonlocal pre, head

        if cur == None:
            return None

        _in_order(cur.left)
        if pre == None:
            head = cur
        else:
            pre.right = cur
            cur.left = pre
        pre = cur

        _in_order(cur.right)

    _in_order(root)
    head.left, pre.right = pre, head
    return head
