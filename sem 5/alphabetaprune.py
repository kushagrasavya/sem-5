def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta):
    # Base case: Leaf node
    if depth == 0 or node_index >= len(values):
        return values[node_index]
    
    if maximizing_player:
        max_eval = float('-inf')
        for i in range(2):  # Two children for binary tree
            eval = alpha_beta_pruning(depth - 1, 2 * node_index + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):  # Two children for binary tree
            eval = alpha_beta_pruning(depth - 1, 2 * node_index + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

# Example usage
values = [3, 5, 6, 9, 1, 2, 0, -1]  # Leaf node values
depth = 3  # Depth of the tree (log2(len(values)))
result = alpha_beta_pruning(depth, 0, True, values, float('-inf'), float('inf'))
print("Optimal value:", result)
