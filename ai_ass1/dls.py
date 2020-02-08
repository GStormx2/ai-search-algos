from actions import make_child_node, path, change_state
from collections import deque
from node import Node
from board import Board
from result import Result
import time

def dls(problem, board, limit):
    #print("\n---------------------------------------\n")
    #print(f"Running DFS with\nState: {problem.state}\nGoal State: {problem.goal}\nLimit: {limit}...")
    
    start = time.perf_counter()
    
    frontier = [problem]
    frontier_size = len(frontier)
    explored = set()
     
    if problem.str_state == problem.goal_str:
        end_prem = time.perf_counter()
        
        return Result(problem, "success", frontier_size, problem.depth, end_prem - start)
    
    while frontier:
        node = frontier.pop()
        #print(len(frontier))
        #print(f"{node.state}")
        if node.depth <= limit:
            
            if node not in explored:
                explored.add(node.str_state)
                
                if node.str_state == node.goal_str:
                    end_final = time.perf_counter()
                    return Result(node, "success", frontier_size, node.depth, end_final - start)
                
                children = reversed(make_child_node(node, node.goal, board))
                for child in children:
                    frontier.append(child)
                if len(frontier) > frontier_size:
                    frontier_size = len(frontier)
    
    end_failed = time.perf_counter()    
    return Result(None, "failed", frontier_size, limit, end_failed - start)