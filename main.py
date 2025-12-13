import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from BackTracking.Algo.backtracking import Backtracking
from BackTracking.Helper.helper import Helper

graph = {
    'a': ['b', 'c'], 
    'b': ['a', 'c'], 
    'c': ['a', 'b'],
    'd' : ['e'],
    'e' : ['d']
}

def start_program():
    print("--- Graph Coloring Problem ---")
    
    try:
        user_input = input("Enter number of colors to use : ")
        num_colors = int(user_input)
    except ValueError:
        print("Error: Please enter a valid number!")
        return
    
    colors_path = os.path.join(current_dir, 'BackTracking', 'Colors', 'color.json')
    selected_colors = Helper.get_colors(colors_path, limit=num_colors)
    
    if not selected_colors:
        print("Error: No colors found or file is missing.")
        return

    print(f"\nAttempting to solve with {len(selected_colors)} colors: {selected_colors}")

    if not Helper.is_graph_connected(graph):
        print("\n WARNING: The graph is DISCONNECTED!")
        print("   (The solver will still work, but check your input if this wasn't intended.)")

    solver = Backtracking(graph, selected_colors)

    result = solver.start_solving()

    # 6. Output Result
    print("\n--- Final Result ---")
    if result:
        print("Success! Here is the coloring:")
        for node in sorted(result.keys()):
            print(f"Node ({node}) --> Color: {result[node]}")
    else:
        print("Failed to find a solution with these colors.")
        print("Try increasing the number of colors.")

if __name__ == "__main__":
    start_program()