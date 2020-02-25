from actions import make_child_node, h_function
from collections import deque
from structures import Result
import time
import heapq

def bfs(problem, board, verbose=False):
    start = time.perf_counter()
    
    with open("log/bfs.txt", "w") as file_obj:
        
        max_depth = 0
        gen_nodes = 0
        
        frontier = deque([problem])
        frontier_size = len(frontier)
        explored = set()
        
        if problem.str_state == problem.goal_str:
            end_prem = time.perf_counter()
            return Result(problem, "success", frontier_size, problem.depth, gen_nodes, end_prem - start)
        
        while frontier:
            if verbose:
                print(f"Frontier before extraction: {len(frontier)}")
                file_obj.write(f"Frontier before extraction: {len(frontier)}\n")
            node = frontier.popleft()
            if verbose:
                print(f"Frontier after extraction: {len(frontier)}")
                file_obj.write(f"Frontier after extraction: {len(frontier)}\n")
            explored.add(node.str_state)
            if verbose:
                print(f"Adding to explored. Current count: {len(explored)}")
                file_obj.write(f"Adding to explored. Current count: {len(explored)}\n")
            
            children = make_child_node(node, node.goal, board)
            if verbose:
                print(f"Generating children nodes..")
                file_obj.write(f"Generating children nodes..\n")
                for child in children:
                    print(f"-> Action: {child.action}, State: {child.state}")
                    file_obj.write(f"-> Action: {child.action}, State: {child.state}\n")
            
            for child in children:
                if verbose:
                    print(f"....Taking child: {child.state}")
                    file_obj.write(f"....Taking child: {child.state}\n")
                gen_nodes = gen_nodes + 1
                if child.str_state not in explored:
                    if verbose:
                        print(f"\tChild not explored. Adding to Frontier & Explored")
                        file_obj.write(f"\tChild not explored. Adding to Frontier & Explored\n")
                    frontier.append(child)
                    explored.add(child.str_state)
                    if len(frontier) > frontier_size:
                        frontier_size = len(frontier)
                    
                    max_depth = child.depth
                    if verbose:
                        print(f"\tCurrent Depth: {max_depth}")
                        file_obj.write(f"\tCurrent Depth: {max_depth}\n")
                    
                    if child.str_state == child.goal_str:
                        end_final = time.perf_counter() 
                        return Result(child, "success", frontier_size, child.depth, gen_nodes, end_final - start)     
                else:
                    if verbose:
                        print(f"\tChild explored. Skipping")
                        file_obj.write(f"\tChild explored. Skipping\n")
            if verbose:
                print(f"Nodes generated: {gen_nodes}")
                file_obj.write(f"Nodes generated: {gen_nodes}\n")
            
    end_failed = time.perf_counter()
    return Result(None, "failed", frontier_size, max_depth, gen_nodes, end_failed - start)

def ucs(problem, board, verbose=False):
    start = time.perf_counter()
    
    with open("log/ucs.txt", "w") as file_obj:
    
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
            if verbose:
                print(f"Frontier (PriorityQ) before extraction: {len(frontier)}")
                file_obj.write(f"Frontier (PriorityQ) before extraction: {len(frontier)}\n")
            _node = heapq.heappop(frontier)
            if verbose:
                print(f"Frontier (PriorityQ) after extraction: {len(frontier)}")
                file_obj.write(f"Frontier (PriorityQ) after extraction: {len(frontier)}\n")
            node = _node[1]
            explored.add(node.str_state)
            if verbose:
                print(f"Adding to explored. Current count: {len(explored)}")
                file_obj.write(f"Adding to explored. Current count: {len(explored)}\n")
            
            if node.str_state == node.goal_str:
                end_final = time.perf_counter()
                return Result(node, "success", frontier_size, max_depth, gen_nodes, end_final - start)
            
            children = make_child_node(node, node.goal, board)
            if verbose:
                print(f"Generating children nodes..")
                file_obj.write(f"Generating children nodes..\n")
                for child in children:
                    print(f"-> Action: {child.action}, State: {child.state}")
                    file_obj.write(f"-> Action: {child.action}, State: {child.state}\n")
            for child in children:
                gen_nodes = gen_nodes + 1
                _node = (child.path_cost, child)
                if verbose:
                    print(f"....Taking child: {child.state}")
                    file_obj.write(f"....Taking child: {child.state}\n")
                if child.str_state not in explored:
                    if verbose:
                        print(f"    Child not explored. Adding to Frontier & Explored")
                        file_obj.write(f"    Child not explored. Adding to Frontier & Explored\n")
                    heapq.heappush(frontier, _node)
                    explored.add(child.str_state)
                    if verbose:
                        print(f"\tAdding child to Map: '{child.str_state}' -> {child}'")
                        file_obj.write(f"\tAdding child to Map: '{child.str_state}' -> {child}\n")
                    mapp[child.str_state] = child
                    
                    if max_depth < child.depth:
                        max_depth = child.depth
                        if verbose:
                            print(f"\tCurrent Depth: {max_depth}")
                            file_obj.write(f"\tCurrent Depth: {max_depth}\n")
                
                elif child.str_state in mapp and child.path_cost < mapp[child.str_state].path_cost:
                    if verbose:
                        print(f"\tBetter than child found in Map\n-> Updating ('{child.str_state}'-> {mapp[child.str_state]}, Cost: {mapp[child.str_state].path_cost} with ('{child.str_state}'-> {child}, Cost: {child.path_cost}))")
                    index = frontier.index((mapp[child.str_state].path_cost, mapp[child.str_state]))
                    frontier[int(index)] = (child.path_cost, child)
                    heapq.heapify(frontier)
                    mapp[child.str_state] = child
                else:
                    if verbose:
                        print(f"\tChild explored. Not a better child. Skipping")
                        file_obj.write("\tChild explored. Not a better child. Skipping\n")
            if verbose:
                print(f"Nodes generated: {gen_nodes}")
                file_obj.write(f"Nodes generated: {gen_nodes}\n")
            
            if len(frontier) > frontier_size:
                frontier_size = len(frontier)

    end_failed = time.perf_counter()
    return Result(None, "failed", frontier_size, max_depth, gen_nodes, end_failed - start)

def dls(problem, board, limit, verbose=False):
    #print("\n---------------------------------------\n")
    #print(f"Running DFS with\nState: {problem.state}\nGoal State: {problem.goal}\nLimit: {limit}...")
    
    start = time.perf_counter()
    
    frontier = [problem]
    frontier_size = len(frontier)
    gen_nodes = 0
    explored = set()
    mapp = {}
     
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
                mapp[node.str_state] = node
                
                if node.str_state == node.goal_str:
                    end_final = time.perf_counter()
                    return Result(node, "success", frontier_size, node.depth, gen_nodes, end_final - start)
                
                children = reversed(make_child_node(node, node.goal, board))
                for child in children:
                    gen_nodes = gen_nodes + 1
                    frontier.append(child)
                if len(frontier) > frontier_size:
                    frontier_size = len(frontier)
            
            elif node.str_state in mapp and node.path_cost < mapp[node.str_state].path_cost:
                explored.remove(node.str_state)
                frontier.append(node)
    
    end_failed = time.perf_counter()    
    return Result(None, "failed", frontier_size, limit, gen_nodes, end_failed - start)

def ids(problem, board, limit, verbose=True):
    result = dls(problem, board, limit)
    
    while result.verdict == "failed":
        #print(f"{result.verdict} for limit {limit}")
        limit = limit + 1
        #print(f"limit increased to {limit}")
        result = dls(problem, board, limit)
    #print(f"found {result.verdict} at limit {limit}")
    return result

def gbfs(problem, board, verbose=True):
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

def a_star(problem, board, verbose=True):
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