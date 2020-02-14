from actions import make_child_node
from node import Node
from board import Board
from result import Result
import time
import heapq

def a_star(problem, board):
    start = time.perf_counter()
    
    frontier_size = 0
    max_depth = 0
    
    problem.h_cost = h_function(problem)
    problem.f_cost = problem.h_cost + problem.path_cost
    _node = (problem.f_cost, problem)
    
    frontier = [_node]
    explored = set()
    entry = {}
    
    heapq.heapify(frontier)
    
    while frontier:
        _node = heapq.heappop(frontier)
        node = _node[1]
        explored.add(node.str_state)
        
        if node.str_state == node.goal_str:
            end_prem = time.perf_counter()
            return Result(node, "success", frontier_size, max_depth, end_prem - start)

                
def h_function(node):
    i = 0
    h = 0
    for x in node.state:
        #print(f"matching {x} with {node.goal[i]}")
        if x != node.goal[i]:
            h = h + 1
            i = i + 1
        else:
            i = i + 1
    return h