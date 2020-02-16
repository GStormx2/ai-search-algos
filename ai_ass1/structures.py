class Node:
    def __init__(self, state, goal, parent, action, depth, path_cost):
        self.state = state
        self.goal = goal
        self.goal_str = ''.join(str(a) for a in self.goal)
        
        self.parent = parent
        self.action = action
        self.depth = depth
        self.path_cost = path_cost
        
        self.h_cost = 0
        self.f_cost = 0
        self.str_state = None
        
        if self.state:
            self.str_state = ''.join(str(a) for a in self.state)
    
    #def __eq__(self, other):
    #    return self.h_cost == other.h_cost
    
    def __lt__(self, other):
        return self.h_cost < other.h_cost

class NodeFCost:
    def __init__(self, state, goal, parent, action, depth, path_cost):
        self.state = state
        self.goal = goal
        self.goal_str = ''.join(str(a) for a in self.goal)
        
        self.parent = parent
        self.action = action
        self.depth = depth
        self.path_cost = path_cost
        
        self.h_cost = 0
        self.f_cost = 0
        self.str_state = None
        
        if self.state:
            self.str_state = ''.join(str(a) for a in self.state)
    
    #def __eq__(self, other):
    #    return self.f_cost == other.f_cost 
    
    def __lt__(self, other):
        return self.f_cost < other.f_cost

class NodeGCost:
    def __init__(self, state, goal, parent, action, depth, path_cost):
        self.state = state
        self.goal = goal
        self.goal_str = ''.join(str(a) for a in self.goal)
        
        self.parent = parent
        self.action = action
        self.depth = depth
        self.path_cost = path_cost
        
        self.h_cost = 0
        self.f_cost = 0
        self.str_state = None
        
        if self.state:
            self.str_state = ''.join(str(a) for a in self.state)
    
    #def __eq__(self, other):
    #    return self.path_cost == other.path_cost    
    
    def __lt__(self, other):
        return self.path_cost < other.path_cost
    
class Board:
    def __init__(self, board_width):
        self.board_width = board_width
        self.board_area = board_width * board_width

class Result:
    def __init__(self, node, verdict, frontier_size, max_depth, gen_nodes, elapsed_time):
        self.node = node
        self.verdict = verdict
        self.frontier_size = frontier_size
        self.max_depth = max_depth
        self.gen_nodes = gen_nodes
        self.elapsed_time = elapsed_time