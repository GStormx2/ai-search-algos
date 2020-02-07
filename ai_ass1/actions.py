from node import Node

def path(node):
    path = []
    while node.parent != None:
        path.append(node.action)
        node = node.parent
    print(path)
    
def make_child_node(node, goal, board):
    children = []
    children.append(Node(change_state(node.state, 'up', board), goal, node, 'up', node.depth + 1, node.path_cost + 1))
    children.append(Node(change_state(node.state, 'down', board), goal, node, 'down', node.depth + 1, node.path_cost + 1))
    children.append(Node(change_state(node.state, 'left', board), goal, node, 'left', node.depth + 1, node.path_cost + 1))
    children.append(Node(change_state(node.state, 'right', board), goal, node, 'right', node.depth + 1, node.path_cost + 1))
    
    new_nodes = [x for x in children if x.state]
    return new_nodes
    

def change_state(state, action, board):
    new_state = state[:]
    x = new_state.index(0)
    
    if action == 'up':
        if x not in range(0, board.board_width):
            temp = new_state[x - board.board_width]
            new_state[x - board.board_width] = new_state[x]
            new_state[x] = temp
            #print(f"up: {new_state}")
            return new_state
        else:
            return None
    if action == 'down':
        if x not in range(board.board_area - board.board_width, board.board_area):
            temp = new_state[x + board.board_width]
            new_state[x + board.board_width] = new_state[x]
            new_state[x] = temp
            #print(f"down: {new_state}")
            return new_state
        else:
            return None
    if action == 'left':
        if x not in range(0, board.board_area, board.board_width):
            temp = new_state[x - 1]
            new_state[x - 1] = new_state[x]
            new_state[x] = temp
            #print(f"left: {new_state}")
            
            return new_state
        else:
            return None
    if action == 'right':
        if x not in range(board.board_width - 1, board.board_area, board.board_width):
            temp = new_state[x + 1]
            new_state[x + 1] = new_state[x]
            new_state[x] = temp
            #print(f"right: {new_state}")
            
            return new_state
        else:
            return None
