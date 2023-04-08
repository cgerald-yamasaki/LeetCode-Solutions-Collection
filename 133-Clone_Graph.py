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
    
# the messy process, if you're curious. This one took my brain a sec

# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if node == None: return None
#         ret_node = Node(node.val)
#         # old_curr = node
#         # new_curr = ret_node
#         old_queue = [node]
#         new_queue = [ret_node]
#         new_nodes_dict = {ret_node.val: ret_node} # val: Node?
#         # new_nodes_set = (ret_node.val)  # set of values of nodes already created
#         while old_queue != []:
#             old_curr = old_queue.pop(0)
#             new_curr = new_queue.pop(0)
#             # new_curr.val = old_curr.val
#             for old_nb in old_curr.neighbors:   # assign new_curr's neighbors
#                 # if old_nb.val not in new_nodes_set:
#                 if old_nb.val not in new_nodes_dict.keys():
#                     new = Node(old_nb.val)
#                     new_nodes_dict[old_nb.val] = new
#                     # new_nodes_set.add(old_nb.val)
#                     old_queue.append(old_nb)
#                     new_queue.append(new)
#                 new_curr.neighbors.append(new_nodes_dict[old_nb.val])
#             print(new_curr.val, new_curr.neighbors)
#         return ret_node
                
            


#          = ret_node
#         # done_vals = set(ret_node.val)
#         done = {}   # dict of val:neighbors

#         node_queue = [node]

#         while node_queue != []:
#             n = node_queue.pop(0)
#             for neigh in n.neighbors:
#                 done.get(neigh.val, -1) # if neigh.val not in done, -1


# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if node == None: return None
#         ret_node = Node(node.val)
#         # new_node = ret_node
#         nodes_done = {} # dict of nodes already done
#         node_queue = [node]
#         new_queue = [ret_node]
#         while node_queue != []:
#             curr_node = node_queue.pop(0)
#             new_node = new_queue.pop(0)
#             # nodes_done.update(new_node.val: )
#             # new_node.val = curr_node.val
#             # new_node.neighbors = curr_node.neighbors
#             for neigh in curr_node.neighbors:
#                 # next_node = Node(neigh.val)   # doens't work cuz makes duplicates
#                 # new_node.neighbors.append(next_node)
#                 if neigh.val not in nodes_done.keys:
#                     node_queue.append(neigh)
#                     new_queue.append(next_node)
#             print(new_node.val, new_node.neighbors)
#         return ret_node


# class Solution:
#     def edge_list(self, node: 'Node') -> List:
#         edge_list = []  # list of [val, neighbor1.val, neighbor2.val...]
#         edgel_queue = [node]    # queue of nodes not done yet
#         done_set = set()    # list of node.vals for nodes already done
#         while edgel_queue != []:
#             curr = edgel_queue.pop(0)
#             new_list = [curr.val]   # new list to be added to edge_list
#             done_set.add(curr.val)
#             for neigh in curr.neighbors:
#                 # if neigh == None: continue
#                 new_list.append(neigh.val)
#                 if neigh.val not in done_set:
#                     edgel_queue.append(neigh)
#             edge_list.append(new_list)
#         return edge_list
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if node == None: return None
#         el = Solution.edge_list(node)
#         ret_node = Node()
#         curr = ret_node

#         def nodeRecur(c: 'Node', orig: 'Node'):
#             c = Node(orig.val)
#             for neigh in orig.neighbors:
#                 nn = Node(nei)
#                 c.neighbors.append()
        
        
#         edge_list = []  # list of [val, neighbor1.val, neighbor2.val...]
#         edgel_queue = [node]    # queue of nodes not done yet
#         done_set = set()    # list of node.vals for nodes already done
#         while edgel_queue != []:
#             curr = edgel_queue.pop(0)
#             new_list = [curr.val]   # new list to be added to edge_list
#             done_set.add(curr.val)
#             for neigh in curr.neighbors:
#                 # if neigh == None: continue
#                 new_list.append(neigh.val)
#                 if neigh.val not in done_set:
#                     edgel_queue.append(neigh)
#             edge_list.append(new_list)
#         print(edge_list)


# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if node == None: return None
#         ret_node = Node(node.val)
#         new_node = ret_node
#         done_set = set(ret_node.val)
#         for neigh in node.neighbors:
#             if neigh.val not in done_set:
#                 nn = Node(neigh.val, [new_node])
#                 new_node.neighbors.append(nn)
#         new_node.neighbors.

#         for neigh in node.neighbors:
#             new_node.neighbors.append()

#         node_queue = [node]
#         while

# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if node == None: return None
#         ret_node = Node(node.val)
#         # new_node = ret_node
#         nodes_done = set() # set of node values of nodes already done
#         node_queue = [node]
#         new_queue = [ret_node]
#         while node_queue != []:
#             curr_node = node_queue.pop(0)
#             new_node = new_queue.pop(0)
#             nodes_done.add(new_node.val)
#             # new_node.val = curr_node.val
#             # new_node.neighbors = curr_node.neighbors
#             for neigh in curr_node.neighbors:
#                 # next_node = Node(neigh.val)   # doens't work cuz makes duplicates
#                 # new_node.neighbors.append(next_node)
#                 if neigh.val not in nodes_done:
#                     node_queue.append(neigh)
#                     new_queue.append(next_node)
#             print(new_node.val, new_node.neighbors)
#         return ret_node
