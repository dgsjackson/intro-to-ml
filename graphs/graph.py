from graphs import node

#Directed Graph
class Graph():

    #edges: [(parent, child), ...]
    def __init__(self, edges):
        self._parse_edges(edges)

    def get_child_ids(self, parent_id):
        return self.edges[parent_id] if parent_id in self.edges else []
    
    def get_parent_ids(self, child_id):
        return self.parents[child_id] if child_id in self.parents else []
    
    def get_ids_breadth_first(self, root_id):
        queue = []
        queued = set()
        order_of_visits = []
        queue.append(root_id)
        queued.add(root_id)
        while len(queue) != 0:
            node = queue.pop(0)
            order_of_visits.append(node)
            if node in self.edges:
                children = self.edges[node]
                next = filter(lambda x: x not in queued, children)
                for node in next:
                    queue.append(node)
                    queued.add(node)
        return order_of_visits
    
    def calc_distance(self, from_idx, to_idx):
        nodes = self.get_nodes_breadth_first(from_idx)
        return nodes[to_idx].distance
    
    def calc_shortest_path(self, from_idx, to_idx):
        nodes = self.get_nodes_breadth_first(from_idx)
        current = to_idx
        path = []
        path.append(current)
        while current != from_idx:
            node = nodes[current]
            path.append(node.previous)
            current = node.previous
        return list(reversed(path))
    
    def get_nodes_breadth_first(self, root_id):
        queue = []
        queued = set()
        nodes = {}
        nodes[root_id] = node.Node(root_id, None, 0)
        queue.append(root_id)
        queued.add(root_id)
        while len(queue) != 0:
            curr_id = queue.pop(0)
            curr_node = nodes[curr_id]
            if (curr_id in self.edges):
                children = self.edges[curr_id]
                for next in filter(lambda c: c not in queued, children):
                    nodes[next] = node.Node(next, curr_id, curr_node.distance + 1)
                    queue.append(next)
                    queued.add(next)
            
        return nodes
    

    def _parse_edges(self, edges):
        children = {}
        parents = {}

        for parent, child in edges:
            if parent not in children:
                children[parent] = [child]
            else:
                children[parent].append(child)
            if child not in parents:
                parents[child] = [parent]
            else:
                parents[child].append(parent)

        self.edges = children
        self.parents = parents


edges = [(0 ,2) , (0 ,3) , (0 ,8) ,(2 ,3) ,(3 ,1) , (3 ,2) , (3 ,5) , (3 ,9) ,(4 ,0) , (4 ,6) , (4 ,8) ,(5 ,7) ,(6 ,3)]
graph = Graph(edges)
print(graph.get_ids_breadth_first(4))