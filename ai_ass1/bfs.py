from actions import make_child_node, path, change_state, path_to_goal
from collections import deque
from node import Node
from board import Board
from test import MyTime
import time

def bfs(problem, board):
    start = time.perf_counter()
    print("\n---------------------------------------\n")
    print(f"Running BFS with\nState: {problem.state}\nGoal State: {problem.goal}\n...")
    frontier_size = 0
    
    frontier = deque([problem])
    explored = set()
    
    if problem.str_state == problem.goal_str:
        print("Goal state found!")
        return
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
                   
                   if child.str_state == child.goal_str:
                       end = time.perf_counter()
                       print("Goal state found!")
                       print(f"Depth: {child.depth}\nFrontier Size: {frontier_size}\nElapsed Time: {end - start}")
                       print("\n---------------------------------------\n")
                       path(child)
                       path_to_goal()   
                       return      
    print("bfs failed")
