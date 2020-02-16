from actions import make_child_node, h_function
from collections import deque
from structures import Result
import time
import heapq

def bfs(problem, board):
    start = time.perf_counter()
    #print("\n---------------------------------------\n")
    #print(f"Running BFS with\nState: {problem.state}\nGoal State: {problem.goal}\n...")
    max_depth = 0
    gen_nodes = 0
    
    frontier = deque([problem])
    frontier_size = len(frontier)
    explored = set()
    
    if problem.str_state == problem.goal_str:
        end_prem = time.perf_counter()
        return Result(problem, "success", frontier_size, problem.depth, gen_nodes, end_prem - start)
    else:
       while frontier:
          # print("Taking a node")
           #print(len(frontier))
           node = frontier.popleft()
           explored.add(node.str_state)
           
           children = make_child_node(node, node.goal, board)
           
           for child in children:
               gen_nodes = gen_nodes + 1
               if child.str_state not in explored:
                   frontier.append(child)
                   explored.add(child.str_state)
                   if len(frontier) > frontier_size:
                       frontier_size = len(frontier)
                   
                   max_depth = child.depth
                   
                   if child.str_state == child.goal_str:
                       end_final = time.perf_counter() 
                       return Result(child, "success", frontier_size, child.depth, gen_nodes, end_final - start)     
    
    end_failed = time.perf_counter()
    return Result(None, "failed", frontier_size, max_depth, gen_nodes, end_failed - start)

def ucs(problem, board):
    start = time.perf_counter()
    
    gen_nodes = 0
    max_depth = 0
    
    _node = (problem.path_cost, problem)
    frontier = [_node]
    frontier_size = len(frontier)
    explored = set()
    mapp = {}
    
    if problem.str_state == problem.goal_str:
        end_prem = time.perf_counter()
        return Result(problem, "success", frontier_size, max_depth, gen_nodes, end_prem - start)
    
    heapq.heapify(frontier)
    
    while frontier:
        _node = heapq.heappop(frontier)
        node = _node[1]
        explored.add(node.str_state)
        
        if node.str_state == node.goal_str:
            end_final = time.perf_counter()
            return Result(node, "success", frontier_size, max_depth, gen_nodes, end_final - start)
        
        children = make_child_node(node, node.goal, board)
        
        for child in children:
            gen_nodes = gen_nodes + 1
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
    return Result(None, "failed", frontier_size, max_depth, gen_nodes, end_failed - start)

def dls(problem, board, limit):
    #print("\n---------------------------------------\n")
    #print(f"Running DFS with\nState: {problem.state}\nGoal State: {problem.goal}\nLimit: {limit}...")
    
    start = time.perf_counter()
    
    
    frontier = [problem]
    frontier_size = len(frontier)
    gen_nodes = 0
    explored = set()
     
    if problem.str_state == problem.goal_str:
        end_prem = time.perf_counter()
        
        return Result(problem, "success", frontier_size, problem.depth, gen_nodes, end_prem - start)
    
    while frontier:
        node = frontier.pop()
        #print(len(frontier))
        #print(f"{node.state}")
        if node.depth <= limit:
            
            if node.str_state not in explored:
                explored.add(node.str_state)
                
                if node.str_state == node.goal_str:
                    end_final = time.perf_counter()
                    return Result(node, "success", frontier_size, node.depth, gen_nodes, end_final - start)
                
                children = reversed(make_child_node(node, node.goal, board))
                for child in children:
                    gen_nodes = gen_nodes + 1
                    frontier.append(child)
                if len(frontier) > frontier_size:
                    frontier_size = len(frontier)
    
    end_failed = time.perf_counter()    
    return Result(None, "failed", frontier_size, limit, gen_nodes, end_failed - start)

def ids(problem, board, limit):
    result = dls(problem, board, limit)
    
    while result.verdict == "failed":
        #print(f"{result.verdict} for limit {limit}")
        limit = limit + 1
        #print(f"limit increased to {limit}")
        result = dls(problem, board, limit)
    #print(f"found {result.verdict} at limit {limit}")
    return result

def gbfs(problem, board):
    start = time.perf_counter()
    
    max_depth = 0
    gen_nodes = 0
    
    problem.h_cost = h_function(problem)
    _node = (problem.h_cost, problem)
    frontier = [_node]
    frontier_size = 0
    explored = set()
    
    if problem.str_state == problem.goal_str:
        end_prem = time.perf_counter()
        return Result(problem, "success", frontier_size, max_depth, gen_nodes, end_prem - start)
   
    heapq.heapify(frontier)
   
    while frontier:
        _node = heapq.heappop(frontier)
        node = _node[1]
        #print(f"prio: {_node[0]} -> node: {node.state}")
        explored.add(node.str_state)
        
        children = make_child_node(node, node.goal, board)
        
        for child in children:
            gen_nodes = gen_nodes + 1
            if child.str_state not in explored:
                child.h_cost = h_function(child)
                _node = (child.h_cost, child)
                heapq.heappush(frontier, _node)
                explored.add(child.str_state)
                
                if max_depth < child.depth:
                    max_depth = child.depth
                
                if child.str_state == child.goal_str:
                    end_final = time.perf_counter()
                    return Result(child, "success", frontier_size, max_depth, gen_nodes, end_final - start)
        
        if len(frontier) > frontier_size:
            frontier_size = len(frontier)
            
        
    end_failed = time.perf_counter()
    return Result(None, "failed", frontier_size, max_depth, gen_nodes, end_failed - start)

def a_star(problem, board):
    start = time.perf_counter()
    
    frontier_size = 0
    max_depth = 0
    gen_nodes = 0
    
    problem.h_cost = h_function(problem)
    problem.f_cost = problem.h_cost + problem.path_cost
    _node = (problem.f_cost, problem)
    
    frontier = [_node]
    explored = set()
    mapp = {}
    
    if problem.str_state == problem.goal_str:
        end_final = time.perf_counter()
        return Result(problem, "success", frontier_size, max_depth, gen_nodes, end_final - start)

    heapq.heapify(frontier)
    
    while frontier:
        _node = heapq.heappop(frontier)
        node = _node[1]
        explored.add(node.str_state)
        
        if node.str_state == node.goal_str:
            end_final = time.perf_counter()
            return Result(node, "success", frontier_size, max_depth, gen_nodes, end_final - start)
        
        children = make_child_node(node, node.goal, board)
        
        for child in children:
            gen_nodes = gen_nodes + 1
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
    return Result(None, "failed", frontier_size, max_depth, gen_nodes, end_failed - start)