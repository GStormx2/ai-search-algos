from actions import make_child_node, path, change_state, path_to_goal
from node import Node
from board import Board
from test import MyTime
from result import Result
import time
import heapq

def gbfs(problem, board):
    start = time.perf_counter()
    frontier_size = 0
    max_depth = 0
    
    problem.h_cost = h_function(problem)
    _node = (problem.h_cost, problem)
    frontier = [_node]
    explored = set()
   
    heapq.heapify(frontier)
   
    while frontier:
        _node = heapq.heappop(frontier)
        node = _node[1]
        explored.add(node.str_state)
        
        if node.str_state == node.goal_str:
            end_prem = time.perf_counter()
            return Result(node, "success", frontier_size, max_depth, end_prem - start)
       
        #print(f"in h_cost {node.h_cost}")
        children = make_child_node(node, node.goal, board)
       
        for child in children:
            if child not in explored:
                child.h_cost = h_function(child)
                _node = (child.h_cost, child)
                heapq.heappush(frontier, _node)
                explored.add(child.str_state)
                
                if len(frontier) > frontier_size:
                    frontier_size = len(frontier)
                
                if max_depth < child.depth:
                    max_depth = child.depth
               
                if child.str_state == child.goal_str:
                    end_final = time.perf_counter()
                    return Result(child, "success", frontier_size, max_depth, end_final - start)
        #heapq.heapify(frontier)
        
    end_failed = time.perf_counter()
    return Result(None, "failed", frontier_size, max_depth, end_failed - start)
            

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