from algorithms import *
from structures import *
from actions import *

def show_statistics(node):
    print(f"Nodes Generated: {node.gen_nodes}")
    print(f"Max Frontier Size: {node.frontier_size}")
    print(f"Max Search Depth: {node.max_depth}")
    print(f"Solution found at depth: {node.node.depth}")
    print(f"Path Cost: {node.node.path_cost}")
    print(f"Elapsed Time: {node.elapsed_time} seconds\n")

node20 = Node([0, 4, 3, 8, 6, 5, 2, 7, 1], [1,2,3,8,0,4,7,6,5], None, None, 0, 0)
result = dls(node20, Board(3), 21)
show_statistics(result)
path(result.node)
path_to_goal()