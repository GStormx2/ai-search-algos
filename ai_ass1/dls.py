from actions import make_child_node, path, change_state
from collections import deque
from node import Node
from board import Board

def dls(problem, board, limit):
    print(f"Running DLS on")
    frontier = [problem]
    explored = set()
     
    if problem.str_state == problem.goal_str:
        print("Goal Found!")
        return
    else:
        while frontier:
            node = frontier.pop()
            print(len(frontier))
            #print(f"{node.state}")
            if node.depth <= limit:
                
                if node not in explored:
                    explored.add(node.str_state)
                    
                    if node.str_state == node.goal_str:
                        print("Goal found!")
                        print(f"depth: {node.depth}")
                        path(node)
                        return
                    
                    children = reversed(make_child_node(node, node.goal, board))
                    for child in children:
                        frontier.append(child)
            else:
                print("limit reached")
    #print("dls failed")