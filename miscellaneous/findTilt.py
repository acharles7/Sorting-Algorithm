"""
Given the root of a binary tree, return the sum of every tree node's tilt.
"""

def findTilt(root: TreeNode) -> int:

    def find_sum(node, add):
        stack = [node]
        while stack:
            last = stack.pop(0)
            add += last.val
            if last.left:
                stack.append(last.left)
            if last.right:
                stack.append(last.right)    
        return add

    if not root: return 0

    stack = [root]
    tilts = 0

    while stack:
        left, right = 0, 0
        last = stack.pop(0)
        if last.left:
            left = find_sum(last.left, 0)
            stack.append(last.left)

        if last.right:
            right = find_sum(last.right, 0)
            stack.append(last.right)

        tilts += abs(left-right)
    return tilts


def findTilt(self, root: TreeNode) -> int:
    tilt = 0

    def find_sum(node):
        nonlocal tilt
        if not node:
            return 0

        left = find_sum(node.left)
        right = find_sum(node.right)
        local_tilt = abs(left-right)
        tilt += local_tilt

        return left+right+node.val

    find_sum(root)
    return tilt

