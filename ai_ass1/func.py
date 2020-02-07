from dls import dls
from bfs import bfs
from node import Node
from board import Board

#random_state = [1,3,4,8,6,2,7,0,5] #easy
#random_state = [2,8,1,0,4,3,7,6,5] #medium
#random_state = [2,8,1,4,6,3,0,7,5] #hard
#random_state = [5,6,7,4,0,8,3,2,1] #worst
random_state = [0,8,7,6,5,4,3,2,1]
#random_state = [3,2,0,1,4,5,6,7,8]

another_goal_state = [0,1,2,3,4,5,6,7,8]
goal_state = [1,2,3,8,0,4,7,6,5]
start_board = Board(3)
start_node = Node(random_state, another_goal_state, None, None, 0, 0)
bfs(start_node, start_board)
#dls(start_node, start_board, 12)