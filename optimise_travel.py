import math
import utm # Coordinates are converted to UTM format for analysis in metres (assume they are in same zone)
import networkx as nx

# NOTE: For the purposes of this exercise we can ignore differing zone letters and numbers
def convert_to_utm_xy(coordinates):
    return [utm.from_latlon(*c)[:2] for c in coordinates]

def calc_total_distance(coordinates_xy, indices):
    total_distance = 0
    for i in range(1, len(indices)):
        dx = coordinates_xy[indices[i]][0] - coordinates_xy[indices[i-1]][0]
        dy = coordinates_xy[indices[i]][1] - coordinates_xy[indices[i-1]][1]
        total_distance += math.sqrt(dx*dx + dy*dy)
    return total_distance

def calc_single_distance(coord_a, coord_b):
    dx = coord_a[0] - coord_b[0]
    dy = coord_a[1] - coord_b[1]
    return math.sqrt(dx*dx + dy*dy)

def optimise_travel_order(coordinates):

    coordinates_xy = convert_to_utm_xy(coordinates)
    indices = list(range(len(coordinates_xy)))
    
    # construct graph 
    graph = nx.Graph()
    graph.add_nodes_from(indices)
    for i in indices:
        for j in indices:
            if i!=j:
                distance = calc_single_distance(coordinates_xy[i], coordinates_xy[j])
                graph.add_edge(i, j, weight=distance)

    # approximation of the travelling salesman problem
    tsp = nx.approximation.traveling_salesman_problem
    # using the default, christofides algorithm 
    # cycle is false as we do not need to return to the beginning
    path = tsp(graph, cycle=False)
    return path


if __name__ == "__main__":
    coordinates = [
            (-36.932197, 174.987783),
            (-36.969210, 174.912630),
            (-37.008773, 174.835551),
            (-36.812159, 174.782783),
            (-36.987639, 174.850803),
            (-36.987525, 174.756794)
        ]

    path = optimise_travel_order(coordinates)
    coords_xy = convert_to_utm_xy(coordinates)
    path_length = calc_total_distance(coords_xy, path)
    print(path)
    print(path_length)
  