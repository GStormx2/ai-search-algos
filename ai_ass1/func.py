from dls import dls
from bfs import bfs
from ids import ids
from node import Node
from board import Board


#random_state = [1,3,4,8,6,2,7,0,5] #easy
#random_state = [2,8,1,0,4,3,7,6,5] #medium
#random_state = [2,8,1,4,6,3,0,7,5] #hard
#random_state = [5,6,7,4,0,8,3,2,1] #worst
#random_state = [0,8,7,6,5,4,3,2,1]
#random_state = [3,2,0,1,4,5,6,7,8]

#another_goal_state = [0,1,2,3,4,5,6,7,8]
#goal_state = [1,2,3,8,0,4,7,6,5]
#start_board = Board(3)
#start_node = Node(random_state, goal_state, None, None, 0, 0)
#bfs(start_node, start_board)
#dls(start_node, start_board, 12)
#some = ids(start_node, start_board, 0)

first_state_goal = []
first_state_start = []

bs = input("Board size: ")
board = Board(bs)

def set_goal():
    print("Goal State: ")
    for x in range(0, bs):
        val = int(input())
        first_state_goal.append(val)

def get_start_node():        
    print("Start State: ")
    for x in range(0, bs):
        val = int(input())
        first_state_start.append(val)
    start_node = Node(first_state_start, first_state_goal, None, None, 0, 0)
    return start_node

running = True
choice = 0

while running:
    print("\n---------------------------------------------------")
    print("Choose and algorithm (1-6) or press 'q' to quit:")
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
    
    if choice == 1:
        print(f"Running BFS on: {first_state_start}")
        print(f"Goal: {first_state_goal}\n...")
        