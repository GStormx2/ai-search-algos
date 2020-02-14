from actions import make_child_node
from collections import deque
from result import Result
import time

def bfs(problem, board):
    start = time.perf_counter()
    #print("\n---------------------------------------\n")
    #print(f"Running BFS with\nState: {problem.state}\nGoal State: {problem.goal}\n...")
    frontier_size = 0
    max_depth = 0
    
    frontier = deque([problem])
    explored = set()
    
    if problem.str_state == problem.goal_str:
        end_prem = time.perf_counter()
        return Result(problem, "success", frontier_size, problem.depth, end_prem - start)
    else:
       while frontier:
          # print("Taking a node")
           #print(len(frontier))
           node = frontier.popleft()
           explored.add(node.str_state)
           
           children = make_child_node(node, node.goal, board)
           
           for child in children:
               if child.str_state not in explored:
                   frontier.append(child)
                   explored.add(child.str_state)
                   if len(frontier) > frontier_size:
                       frontier_size = len(frontier)
                   
                   max_depth = child.depth
                   
                   if child.str_state == child.goal_str:
                       end_final = time.perf_counter() 
                       return Result(child, "success", frontier_size, child.depth, end_final - start)     
    
    end_failed = time.perf_counter()
    return Result(None, "failed", frontier_size, max_depth, end_failed - start)
