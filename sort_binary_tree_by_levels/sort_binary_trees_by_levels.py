'''Sort binary tree by levels'''
from collections import deque
def tree_by_levels(node):
    '''BFS'''
    if node is None:
        return []
    queue = deque([node])
    result = []
    while queue:
        cur_node = queue.popleft()
        result.append(cur_node.value)

        if cur_node.left is not None:
            queue.append(cur_node.left)
        if cur_node.right is not None:
            queue.append(cur_node.right)

    return result
