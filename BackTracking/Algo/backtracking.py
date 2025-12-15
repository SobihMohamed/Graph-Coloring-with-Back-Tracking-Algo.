class Backtracking:
    def __init__(self, graph, colors_list, analytics=None):
        self.graph = graph
        self.colors = colors_list
        self.nodes = self.get_connected_order(graph)
        self.solution = {}
        self.analytics = analytics

    def get_connected_order(self, graph):
        if not graph:
            return []
            
        # ترتيب المفاتيح عشان نضمن البداية من الأصغر
        sorted_keys = sorted(list(graph.keys()), key=lambda x: int(x))
        
        visited = set()
        ordered_nodes = []
        
        # دالة مساعدة للـ DFS (Recursive)
        def dfs_visit(u):
            visited.add(u)
            ordered_nodes.append(u)
            
            # هات الجيران ورتبهم
            neighbors = graph.get(u, [])
            # رتبهم عشان نمشي بالترتيب الصغير للكبير جوه الفرع
            neighbors = sorted(neighbors, key=lambda x: int(x))
            
            for v in neighbors:
                if v not in visited:
                    dfs_visit(v)

        # اللوب عشان لو الجراف مفصول (Disconnected)
        for start_node in sorted_keys:
            if start_node not in visited:
                dfs_visit(start_node)
                            
        return ordered_nodes
    
    
    # ! Standard Backtracking
    def is_safe(self, node, color):
        for neighbor in self.graph.get(node, []):
            if neighbor in self.solution and self.solution[neighbor] == color:
                return False
        return True

    def solve_standard(self, node_index=0):
        if self.analytics:
          self.analytics.increment_visited_nodes()
        
        if node_index == len(self.nodes):
          return True
        
        current_node = self.nodes[node_index]
        
        #! Brute-force approach within backtracking
        for color in self.colors:
            if self.is_safe(current_node, color):
                self.solution[current_node] = color
                if self.solve_standard(node_index + 1):
                  return True
                
                if self.analytics: 
                  self.analytics.increment_backtracks()
                
                del self.solution[current_node]

        return False

    #! Optimized Backtracking
    def get_valid_colors(self, node):
        neighbors = self.graph.get(node, [])
        forbidden = {self.solution[n] for n in neighbors if n in self.solution}
        #? Return only colors that are not forbidden
        return [c for c in self.colors if c not in forbidden]

    def solve_optimized(self, node_index=0):
        if self.analytics: 
            self.analytics.increment_visited_nodes()
        
        if node_index == len(self.nodes):
          return True
        
        current_node = self.nodes[node_index]
        
        #? Domain Reduction
        valid_colors = self.get_valid_colors(current_node)
        
        for color in valid_colors:
            self.solution[current_node] = color
            if self.solve_optimized(node_index + 1):
              return True
            
            if self.analytics:
              self.analytics.increment_backtracks()
              
            del self.solution[current_node]

        return False

    #! Entry Points
    def start_standard_solve(self):
        if self.analytics:
          self.analytics.start_timer()
        self.solution = {}

        result = self.solve_standard(0)
        if self.analytics:
          self.analytics.stop_timer(success=result)

        return self.solution if result else None

    def start_optimal_solve(self):
        if self.analytics:
            self.analytics.start_timer()

        original_colors = self.colors.copy()
        
        for k in range(1, len(original_colors) + 1):
            self.colors = original_colors[:k]
            self.solution = {}

            if self.solve_optimized(0):
                if self.analytics:
                    self.analytics.stop_timer(success=True)
                return k, self.solution
        
        if self.analytics:
            self.analytics.stop_timer(success=False)
            
        return -1, None