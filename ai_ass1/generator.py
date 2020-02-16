from actions import make_child_node
from structures import Node, Board
from collections import deque
import time
import random

def unleash_chaos():
    goal_state = [0, 1, 2, 3 ,4 ,5, 6, 7, 8]
    board = Board(3)
    node = Node(goal_state, goal_state, None, None, 0, 0)
    frontier = deque([node])
    depth = 0
    explored = set()
    
    entry = {}
    
    for x in range(1, 21, 1):
        entry[x] = []
    
    while frontier:
        _node = frontier.popleft()
        explored.add(_node)
        
        children = make_child_node(_node, _node.goal, board)
        
        for child in children:
            if child.depth > 20:
                break
            
            if child.str_state not in explored:
                explored.add(child.str_state)
                frontier.append(child)
                depth = child.depth
                
                if child.str_state != child.goal_str:
                    entry[child.depth].append(child.state)
            
        print(f"Depth: {depth}")
    
    print(entry)
    
    for depth, item in entry.items():
        x = random.randrange(0, len(item), 1)
        new = item[x]
        entry[depth] = new
    
    for depth, item in entry.items():
        print(f"Depth #{depth} -> {item}")

def run_algos(problem, board, limit):
    print("not implemented")

if __name__ == "__main__":
    unleash_chaos()