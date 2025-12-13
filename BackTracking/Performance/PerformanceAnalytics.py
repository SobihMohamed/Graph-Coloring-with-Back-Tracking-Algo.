import time

class PerformanceAnalytics:
    def __init__(self):
        self.reset()

    def reset(self):
        self.start_time = 0
        self.end_time = 0
        self.execution_time_ms = 0
        self.nodes_visited = 0    
        self.backtracks_count = 0 
        self.solution_found = False

    def start_timer(self):
        self.reset()
        self.start_time = time.perf_counter() 

    def stop_timer(self, success=False):
        self.end_time = time.perf_counter()

        self.execution_time_ms = (self.end_time - self.start_time) * 1000
        self.solution_found = success

    def increment_visited_nodes(self):
        self.nodes_visited += 1

    def increment_backtracks(self):
        self.backtracks_count += 1