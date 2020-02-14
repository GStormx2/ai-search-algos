from actions import make_child_node
from result import Result
import time
import heapq

def ucs(problem, board):
    start = time.perf_counter()
    
    frontier_size = 0
    max_depth = 0
    
    _node = (problem.path_cost, problem)
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
            _node = (child.path_cost, child)
            
            if child.str_state not in explored:
                heapq.heappush(frontier, _node)
                explored.add(child.str_state)
                mapp[child.str_state] = child
                
                if max_depth < child.depth:
                    max_depth = child.depth
            
            elif child.str_state in mapp and child.path_cost < mapp[child.str_state].path_cost:
                
                index = frontier.index((mapp[child.str_state].path_cost, mapp[child.str_state]))
                frontier[int(index)] = (child.path_cost, child)
                heapq.heapify(frontier)
                mapp[child.str_state] = child
        
        if len(frontier) > frontier_size:
            frontier_size = len(frontier)

    end_failed = time.perf_counter()
    return Result(None, "failed", frontier_size, max_depth, end_failed - start)