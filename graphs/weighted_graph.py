from graphs import node

class WeightedGraph():

    def __init__(self, weights):
        self.weights = weights
        self.nodes = {}
        self.edges = {}
        self._parse_edges()

    def _parse_edges(self):
        for parent, child in list(self.weights):
            if parent not in self.edges:
                self.edges[parent] = [child]
            else:
                self.edges[parent].append(child)
            if parent not in self.nodes:
                self.nodes[parent] = node.Node(parent, previous=None, distance=None)
            if child not in self.nodes:
                self.nodes[child] = node.Node(child, previous=None, distance=None)
    
    def calc_distance(self, from_idx, to_idx):
        self.nodes[from_idx].distance = 0
        current_idx = from_idx
        visited = [current_idx]
        while current_idx != to_idx:
            neighbours = self.edges[current_idx]
            for n_idx in neighbours:
                current_node = self.nodes[current_idx]
                n_node = self.nodes[n_idx]
                if n_node.distance == None or n_node.distance > current_node.distance + self.weights[(current_idx, n_idx)]:
                    n_node.distance = current_node.distance + self.weights[(current_idx, n_idx)]
                    n_node.previous = current_idx
            nearest = self._get_nearest_node_to_visited(visited)
            visited.append(nearest.id)
            current_idx = nearest.id
        return self.nodes[current_idx].distance


    def calc_shortest_path(self, from_idx, to_idx):
        #look up previous values starting from to_idx
        return
    
    def _get_nearest_node_to_visited(self, visited):
        min = None
        min_node = None
        for node in filter(lambda x: x.id not in visited, self.nodes.values()):
            if node.distance != None and (min == None or node.distance < min):
                min = node.distance
                min_node = node

        return min_node