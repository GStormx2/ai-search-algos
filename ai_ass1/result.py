class Result:
    def __init__(self, node, verdict, frontier_size, max_depth, elapsed_time):
        self.node = node
        self.verdict = verdict
        self.frontier_size = frontier_size
        self.max_depth = max_depth
        self.elapsed_time = elapsed_time