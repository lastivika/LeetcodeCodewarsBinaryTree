'''Binary Tree Traversal'''
# Pre-order traversal
def pre_order(node):
    '''root -> left node -> right node'''
    if node is None:
        return []
    return [node.data]+pre_order(node.left)+pre_order(node.right)


# In-order traversal
def in_order(node):
    '''left leaf -> root -> right leaf'''
    if node is None:
        return []
    return in_order(node.left)+[node.data]+in_order(node.right)

# Post-order traversal
def post_order(node):
    '''leaves -> root'''
    if node is None:
        return []
    return post_order(node.left)+post_order(node.right)+[node.data]
