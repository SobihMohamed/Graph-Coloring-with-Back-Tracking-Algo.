import json

class Helper:
  @staticmethod
  def get_colors(file_path,limit=None):
    try:
      with open(file_path,'r') as file:
        data = json.load(file)
        colors = data.get("all_colors",[])
        # check if has limit and less than size of colors available
        if limit and limit <= len(colors) :
          return colors[:limit]
        
        print("Warning : Limit exceeds available colors, returning all colors.")
        return colors
    except FileNotFoundError:
      print("Error : Colors File Not Found.")
      return []
    except Exception as e :
      print(f"Error Occurred While Reading : {e}")
      return []
  
  #Examople
  ##graph = {
    # 'A': ['B'],
    # 'B': ['A', 'C'],
    # 'C': ['B'],

    # 'D': ['E'],     
    # 'E': ['D']
    # }
  ##

  @staticmethod
  def is_graph_connected(graph):
    if not graph:
      return True
    nodes = list(graph.keys()) # A , B, C, D, E
    start_node = nodes[0] # start from first node => A

    visited = set() # to track visited nodes and avoid cycles[no repeat]
    queue = [start_node] # initialize queue with start node
    visited.add(start_node) # mark A as visited

    while queue:
      current = queue.pop(0)  # dequeue => A
      neighbors_of_current = graph.get(current, []) # get neighbors or empty list => ['B']
      for neighbor in neighbors_of_current:
        if neighbor not in visited: # if not visited
          visited.add(neighbor) # mark as visited
          queue.append(neighbor) # add to queue for exploration

    if len(visited) == len(nodes):
      return True
    return False
