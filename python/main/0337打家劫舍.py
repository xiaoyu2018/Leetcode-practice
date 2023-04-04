from binarytree import TreeNode, level_create

# 暴力递归
def rob1(root: TreeNode) -> int:
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return root.val

    # 偷root
    val1 = root.val
    if root.left:
        val1 += rob1(root.left.left) + rob1(root.left.right)
    if root.right:
        val1 += rob1(root.right.left) + rob1(root.right.right)
    # 不偷root
    val2 = rob1(root.left) + rob1(root.right)

    return max(val1, val2)


# 动态规划
# dp数组为偷与不偷当前节点能得到的最大金钱
def rob2(root: TreeNode) -> int:
    def _rob(crt: TreeNode) -> list:
        if not crt:
            return 0, 0

        # 需要先知道子树的信息
        ls, ln = _rob(crt.left)
        rs, rn = _rob(crt.right)

        return crt.val + ln + rn, max(ls, ln) + max(rs, rn)

    return max(_rob(root))


print(rob2(level_create([3, 2, 3, None, 3, None, 1])))
