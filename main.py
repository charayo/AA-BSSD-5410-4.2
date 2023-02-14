from Graph import *


def load_graph(g):
    g.add_vertex('g')  # Gilroy, CA
    g.add_vertex('l')  # Lubbock Tx
    g.add_vertex('t')  # Tupelo, MS
    g.add_vertex('c')  # Cheyenne, WY
    g.add_vertex('f')  # Fargo, ND
    g.add_vertex('z')  # Zanesville, OH
    g.add_vertex('w')  # Worcester, MA

    g.add_edge('g', 'c', 941, True)
    g.add_edge('c', 'l', 548, True)
    g.add_edge('c', 'f', 562, True)
    g.add_edge('l', 'g', 1134, True)
    g.add_edge('l', 'f', 958, True)
    g.add_edge('l', 'z', 1182, True)
    g.add_edge('t', 'l', 757, True)
    g.add_edge('t', 'z', 539, True)
    g.add_edge('f', 'z', 881, True)
    g.add_edge('z', 'w', 555, True)
    g.add_edge('w', 't', 1069, True)


# end def load_graph():


def path_to_target(start, goal, g):
    dijkstra(g, g.get_vertex(start), g.get_vertex(goal))
    target = g.get_vertex(goal)
    path = [target.get_id()]
    shortest(target, path)
    return path[::-1], target.get_distance()


def reset_visited_and_distance(g):
    for v in g:
        v.set_distance(sys.maxsize)
        v.clear_visited()
#   end def reset_visited_and_distance(g):


def shortest_routes(start, target, graph):
    dict_of_places = {'g': 'Gilroy', 'l': 'Lubbock', 't': 'Tupelo', 'c': 'Cheyenne', 'f': 'Fargo', 'z': 'Zanesville',
                      'w': 'Worcester'}

    # The shortest routes to visit from Gilroy to Lubbock
    target_path, distance = path_to_target(start, target, graph)
    result = "The shortest route is to move from {}, ".format(dict_of_places[start])
    paths = target_path[1:-1]
    for city in paths:
        result += f"to {dict_of_places[city]},"
    result += " and finally to {}. Which is a distance of {}.".format(dict_of_places[target], distance)
    print(result)
    reset_visited_and_distance(graph)


def main():
    graph = Graph()
    load_graph(graph)
    print("===========================================================================================================")
    shortest_routes('g', 'l', graph)
    shortest_routes('g', 'z', graph)
    shortest_routes('t', 'f', graph)
    # shortest_routes('w', 'g', graph)
    print("===========================================================================================================")


if __name__ == '__main__':
    main()
