from result import Result
from dls import dls

def ids(problem, board, limit):
    result = dls(problem, board, limit)
    
    while result.verdict == "failed":
        print(f"{result.verdict} for limit {limit}")
        limit = limit + 1
        print(f"limit increased to {limit}")
        result = dls(problem, board, limit)
    print(f"found {result.verdict} at limit {limit}")
    return result