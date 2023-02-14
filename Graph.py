# Code gotten from:
#   https://www.bogotobogo.com/python/python_graph_data_structures.php
#   https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
# License: Copyright © 2020, bogotobogo
# Accessed on: 02/11/23
# Changelog:
#   Added directed boolean to the add_edge method

import sys
import heapq


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def __lt__(self, other):
        return self.get_distance() < other.get_distance()

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def set_visited(self):
        self.visited = True

    def clear_visited(self):
        self.visited = False


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0, directed=False):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)

        if not directed:
            if to not in self.vert_dict:
                self.add_vertex(to)
            self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous


def shortest(v, path):
    ''' make the shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return
# iterative


def dijkstra(aGraph, start, target):
    print
    '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(), v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        # for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                # print(
                #     'updated : current = %s next = %s new_dist = %s'
                #     % (current.get_id(), next.get_id(), next.get_distance()))
            else:
                response = 'not updated : current = %s next = %s new_dist = %s' % (
                    current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(), v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)


if __name__ == '__main__':

    g = Graph()

    g.add_vertex('s')  # start (book)
    g.add_vertex('b')  # bass guitar
    g.add_vertex('p')  # poster
    g.add_vertex('d')  # drum set
    g.add_vertex('r')  # rare LP
    g.add_vertex('g')  # goal (piano)

    g.add_edge('s', 'r', 5, True)
    g.add_edge('s', 'p', 0, True)
    g.add_edge('r', 'b', 15, True)
    g.add_edge('r', 'd', 20, True)
    g.add_edge('p', 'd', 35, True)
    g.add_edge('p', 'b', 30, True)
    g.add_edge('d', 'g', 10, True)
    g.add_edge('b', 'g', 20, True)

    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            # print('( %s , %s, %3d)' % (vid, wid, v.get_weight(w)))

    dijkstra(g, g.get_vertex('s'), g.get_vertex('g'))

    target = g.get_vertex('g')
    path = [target.get_id()]
    shortest(target, path)
    print('The shortest path : %s' % (path[::-1]))
