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
        
    def __lt__(self, other):
            return self.h_cost < other.h_cost