from actions import make_child_node, path, path_to_goal
from algorithms import bfs, ucs, dls, ids, gbfs, a_star
from structures import Node, NodeFCost, NodeGCost, Board
from collections import deque
import sys
import json
import pprint
import time
import random

def unleash_chaos():
    goal_state = [1,2,3,8,0,4,7,6,5]
    board = Board(3)
    
    print(f"Generating random states from\nGoal: {goal_state}\nBoard Size: 3x3")
    
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
            
        #print(f"Depth: {depth}")
    
    #print(entry)
    print("Unique states generated for all depth 1 to 20!")
    for depth, item in entry.items():
        x = random.randrange(0, len(item), 1)
        new = item[x]
        entry[depth] = new
    print("Picking a random state for each depth..")
    for depth, item in entry.items():
        print(f"Depth #{depth} -> {item}")
    
    print("Running all the algos for each depth (1 to 20):\n")
    run_algos(entry, goal_state, board)

def run_algos(state_dict, goal, board):
    
    entry = {}
    for x in range(1, 21, 1):
        entry[x] = {
            "time": 1.0,
            "nodes": 1,
            "cost": 1
        }
    
    #BFS
    sys.stdout.write("Generating stats for BFS..")         
    for x in range(1, 21):
        result = bfs(Node(state_dict[x], goal, None, None, 0, 0), board)
        if result.verdict == "success":
            entry[x]["time"] = result.elapsed_time
            entry[x]["nodes"] = result.gen_nodes
            entry[x]["cost"] = result.node.path_cost
            sys.stdout.write(f" #{x},")
        else:
            entry[x]["time"] = 0.0
            entry[x]["nodes"] = 0
            entry[x]["cost"] = 0
            sys.stdout.write(f" #{x}(F),")
    print("")
    write_file(entry, "bfs")
    clear_dict(entry)
    
    #DLS
    sys.stdout.write("Generating stats for DLS..")         
    for x in range(1, 21):
        result = dls(Node(state_dict[x], goal, None, None, 0, 0), board, x+1)
        if result.verdict == "success":
            entry[x]["time"] = result.elapsed_time
            entry[x]["nodes"] = result.gen_nodes
            entry[x]["cost"] = result.node.path_cost
            sys.stdout.write(f" #{x},")
        else:
            entry[x]["time"] = 0.0
            entry[x]["nodes"] = 0
            entry[x]["cost"] = 0
            sys.stdout.write(f" #{x}(F),")
    print("")
    write_file(entry, "dls")
    clear_dict(entry)
    
    #IDS
    sys.stdout.write("Generating stats for IDS..")         
    for x in range(1, 21):
        result = ids(Node(state_dict[x], goal, None, None, 0, 0), board, 0)
        if result.verdict == "success":
            entry[x]["time"] = result.elapsed_time
            entry[x]["nodes"] = result.gen_nodes
            entry[x]["cost"] = result.node.path_cost
            sys.stdout.write(f" #{x}")
        else:
            entry[x]["time"] = 0.0
            entry[x]["nodes"] = 0
            entry[x]["cost"] = 0
            sys.stdout.write(f" #{x}(F),")
    print("")
    write_file(entry, "ids")
    clear_dict(entry)
    
    #UCS
    sys.stdout.write("Generating stats for UCS..")         
    for x in range(1, 21):
        result = ucs(NodeGCost(state_dict[x], goal, None, None, 0, 0), board)
        if result.verdict == "success":
            entry[x]["time"] = result.elapsed_time
            entry[x]["nodes"] = result.gen_nodes
            entry[x]["cost"] = result.node.path_cost
            sys.stdout.write(f" #{x},")
        else:
            entry[x]["time"] = 0.0
            entry[x]["nodes"] = 0
            entry[x]["cost"] = 0
            sys.stdout.write(f" #{x}(F),")
    print("")
    write_file(entry, "ucs")
    clear_dict(entry)
    
    #GBFS
    sys.stdout.write("Generating stats for GBFS..")         
    for x in range(1, 21):
        result = gbfs(Node(state_dict[x], goal, None, None, 0, 0), board)
        if result.verdict == "success":
            entry[x]["time"] = result.elapsed_time
            entry[x]["nodes"] = result.gen_nodes
            entry[x]["cost"] = result.node.path_cost
            sys.stdout.write(f" #{x},")
        else:
            entry[x]["time"] = 0.0
            entry[x]["nodes"] = 0
            entry[x]["cost"] = 0
            sys.stdout.write(f" #{x}(F),")
    print("")
    write_file(entry, "gbfs")
    clear_dict(entry)
    
    #ASTAR
    sys.stdout.write("Generating stats for A*..")         
    for x in range(1, 21):
        result = a_star(NodeFCost(state_dict[x], goal, None, None, 0, 0), board)
        if result.verdict == "success":
            entry[x]["time"] = result.elapsed_time
            entry[x]["nodes"] = result.gen_nodes
            entry[x]["cost"] = result.node.path_cost
            sys.stdout.write(f" #{x},")
        else:
            entry[x]["time"] = 0.0
            entry[x]["nodes"] = 0
            entry[x]["cost"] = 0
            sys.stdout.write(f" #{x}(F),")
    print("")
    write_file(entry, "astar")
    clear_dict(entry)
    
def write_file(entry, name):
    path = "data/" + name + ".json"
    with open(path, "w") as file_obj:
        json.dump(entry, file_obj)
    print(f"written to {path}\n")
    
def clear_dict(entry):
    for x in range(1, 21, 1):
        entry[x] = {
            "time": 0.0,
            "nodes": 0,
            "cost": 0
        }
if __name__ == "__main__":
    unleash_chaos()