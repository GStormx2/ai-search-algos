from actions import make_child_node, path, change_state, path_to_goal
from dls import dls
from bfs import bfs
from ids import ids
from gbfs import gbfs
from node import Node
from board import Board
from result import Result


#start_state = [1,3,4,8,6,2,7,0,5] #easy
#start_state = [2,8,1,0,4,3,7,6,5] #medium
start_state = [2,8,1,4,6,3,0,7,5] #hard
#random_state = [5,6,7,4,0,8,3,2,1] #worst
#random_state = [0,8,7,6,5,4,3,2,1]
#random_state = [3,2,0,1,4,5,6,7,8]

#another_goal_state = [0,1,2,3,4,5,6,7,8]
goal_state = [1,2,3,8,0,4,7,6,5]
board = Board(3)
start_node = Node(start_state, goal_state, None, None, 0, 0)
#bfs(start_node, start_board)
#dls(start_node, start_board, 12)
#some = ids(start_node, start_board, 0)

#goal_state = []
#start_state = []

def set_goal(size):
    print("Goal State: ")
    for x in range(0, size*size):
        val = int(input())
        goal_state.append(val)

def get_start_node(size):        
    print("Start State: ")
    for x in range(0, size*size):
        val = int(input())
        start_state.append(val)
    start_node = Node(start_state, goal_state, None, None, 0, 0)
    return start_node

def show_statistics(node):
    print(f"Frontier Size: {node.frontier_size}")
    print(f"Max Depth: {node.max_depth}")
    print(f"Elapsed Time: {node.elapsed_time}\n")
    
def main():
    
    #bs = int(input("Board size: "))
    #board = Board(bs)
    
    #set_goal(bs)
    #start_node = get_start_node(bs)
    
    running = True
    choice = 0
    
    while running:
        print("\n---------------------------------------------------")
        print("Choose and algorithm (1-6) or press 0 to quit:")
        print("1. Breadth-First Search (BFS)")
        print("2. Uninformed Cost Search (UCS)")
        print("3. Depth Limited Search (DLS)")
        print("4. Iterativee Deepening Depth-First Search (IDS)")
        print("5. Greedy Best-First Search (GBFS)")
        print("6. A* Search")
        try:
            choice = int(input("Choice: "))
        except:
            print("Only interger input allowed")
            continue
        
        if choice == 0:
            break
        
        elif choice == 1:
            print(f"Running BFS on: {start_state}")
            print(f"Goal: {goal_state}\n...")
            result = bfs(start_node, board)
            if result.verdict == 'success':
                print("Goal State Found!")
                show_statistics(result)
                path(result.node)
                path_to_goal()
            elif result.verdict == 'failed':
                print("Goal Not Found")
        
        elif choice == 5:
            print(f"Running GBFS on: {start_state}")
            print(f"Goal: {goal_state}\n...")
            result = gbfs(start_node, board)
            if result.verdict == 'success':
                print("Goal State Found!")
                show_statistics(result)
                path(result.node)
                path_to_goal()
            elif result.verdict == 'failed':
                print("Goal Not Found")

if __name__ == '__main__':
    main()
            