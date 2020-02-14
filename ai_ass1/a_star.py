from actions import make_child_node
from result import Result
import time
import heapq

def a_star(problem, board):
    start = time.perf_counter()
    
    frontier_size = 0
    max_depth = 0
    
    problem.h_cost = h_function(problem)
    problem.f_cost = problem.h_cost + problem.path_cost
    _node = (problem.f_cost, problem)
    
    frontier = [_node]
    explored = set()
    mapp = {}
    
    heapq.heapify(frontier)
    
    while frontier:
        _node = heapq.heappop(frontier)
        node = _node[1]
        explored.add(node.str_state)
        
        if node.str_state == node.goal_str:
            end_prem = time.perf_counter()
            return Result(node, "success", frontier_size, max_depth, end_prem - start)
        
        children = make_child_node(node, node.goal, board)
        
        for child in children:
            child.h_cost = h_function(child)
            child.f_cost = child.h_cost + child.path_cost
            _node = (child.f_cost, child)
            
            if child.str_state not in explored:
                heapq.heappush(frontier, _node)
                explored.add(child.str_state)
                mapp[child.str_state] = child
                
                if max_depth < child.depth:
                    max_depth = child.depth
            
            elif child.str_state in mapp and child.f_cost < mapp[child.str_state].f_cost:
                index = frontier.index((mapp[child.str_state].f_cost, mapp[child.str_state]))
                frontier[int(index)] = (child.f_cost, child)
                heapq.heapify(frontier)
                mapp[child.str_state] = child
        
        if len(frontier) > frontier_size:
            frontier_size = len(frontier)
    
    end_failed = time.perf_counter()
    return Result(None, "failed", frontier_size, max_depth, end_failed - start)

def h_function(node):
    i = 0
    h = 0
    for x in node.state:
        #print(f"matching {x} with {node.goal[i]}")
        if x != node.goal[i]:
            h = h + 1
            i = i + 1
        else:
            i = i + 1
    return h