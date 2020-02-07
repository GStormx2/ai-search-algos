from actions import make_child_node, path, change_state
from collections import deque
from node import Node
from board import Board


def bfs(problem, board):
    frontier = deque([problem])
    explored = set()
    
    if problem.str_state == problem.goal_str:
        print("Goal state found!")
        return
    else:
       while frontier:
          # print("Taking a node")
           print(len(frontier))
           node = frontier.popleft()
           explored.add(node.str_state)
           
           children = make_child_node(node, node.goal, board)
           
           for child in children:
               if child.str_state not in explored:
                   frontier.append(child)
                   explored.add(child.str_state)
                   
                   if child.str_state == child.goal_str:
                       print("Goal state found!")
                       print(f"depth: {child.depth}")
                       path(child)   
                       return      
    print("bfs failed")
