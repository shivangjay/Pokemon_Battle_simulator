# In expression tree, the integer values will be at the leaf nodes
# The operands will be all the other internal nodes/parent nodes to the 2 int leaf nodes

class Node:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def evaluate(root):
    if root is None:
        return 0

    # Check for leaf node
    if root.left is None and root.right is None:
        return int(root.data)

    # Evaluate left tree
    left_sum = evaluate(root.left)

    # Evaluate right tree
    right_sum = evaluate(root.right)

    # Check which operator to apply
    if root.data == '+':
        return left_sum + right_sum

    elif root.data == '-':
        return left_sum - right_sum

    elif root.data == '*':
        return left_sum * right_sum
    
    elif root.data == '**':
        return left_sum ** right_sum

    elif root.data == 'SQRT':
        return left_sum.sqrt(right_sum)
    
    else:
        return left_sum / right_sum
