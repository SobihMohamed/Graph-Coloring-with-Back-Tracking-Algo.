class Backtracking:
    def __init__(self, graph, colors_list , analytics = None):
        self.graph = graph
        self.colors = colors_list
        self.nodes = list(graph.keys())
        self.solution ={} 
        self.analytics = analytics

    def is_safe(self, node, color):
        neighbors_of_node = self.graph.get(node, [])
        for neighbor in neighbors_of_node:
            if neighbor in self.solution  and self.solution[neighbor] == color:
                return False
        return True
    
    def solve (self, node_index=0):
        if self.analytics:
            self.analytics.increment_visited_nodes()

        if node_index == len(self.nodes):
            return True
        current_node = self.nodes[node_index]
        for color in self.colors:
            if self.is_safe(current_node, color):
                self.solution[current_node] = color
                if self.solve(node_index + 1):
                    return True
                
                if self.analytics:
                    self.analytics.increment_backtracks()

                del self.solution[current_node]

        return False
    
    def start_solving(self):
            if self.analytics:
                self.analytics.start_timer()
                
            self.solution = {}  
            result = self.solve(0)

            if self.analytics:
                self.analytics.stop_timer(success=result)

            if result:
                return self.solution
            else:
                return None