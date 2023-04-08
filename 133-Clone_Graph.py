# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# works, 92.99th percentile for runtime, 65.11th for memory
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None: return None
        ret_node = Node(node.val)
        old_queue = [node]
        new_queue = [ret_node]
        new_nodes_dict = {ret_node.val: ret_node} # val: Node
        while old_queue != []:
            old_curr = old_queue.pop(0)
            new_curr = new_queue.pop(0)
            for old_nb in old_curr.neighbors:   # assign new_curr's neighbors
                if old_nb.val not in new_nodes_dict.keys():
                    new = Node(old_nb.val)
                    new_nodes_dict[old_nb.val] = new
                    old_queue.append(old_nb)
                    new_queue.append(new)
                new_curr.neighbors.append(new_nodes_dict[old_nb.val])
        return ret_node
