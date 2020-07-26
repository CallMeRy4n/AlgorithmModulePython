from collections import namedtuple, deque

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

def create_Edge(start, end, cost):
    return Edge(start, end, cost)

class Dijstra():
    def __init__(self, edges: list):
        is_error = [val for val in edges if len(val) not in [2, 3]]
        if is_error:
            raise ValueError("Wrong value: {0}".format(is_error))
        self.edges = [create_Edge(*edge) for edge in edges]

    @property
    def node(self):
        return set(
            sum(([edge.start, edge.end] for edge in self.edges), [])
        )
        '''
        EX: o = ([1, 2], [3, 4])
        i = []
        sum(o, i) => [1, 2, 3, 4]
        set(sum(o, i)) => {1, 2, 3, 4}
        '''
    
    @property
    def neighbours(self):
        neighbours = {node: set() for node in self.node}
        for edge in self.edges:
            val = (edge.end, edge.cost)
            neighbours[edge.start].add(val)
        # set(list) alway return {value}
        return neighbours

    def dijstra(self, startNode, endNode):
        '''
        Returns: 
            list: shortest path, contain each node
        '''

        # Code start
        assert startNode in self.node, 'Such source node doesn\'t exist'
        distance = {point: inf for point in self.node}
        before = {point: None for point in self.node}
        distance[startNode] = 0
        node = self.node.copy()

        while node:
            current_node = min(node, key=lambda v: distance[v])# picking next node
            node.remove(current_node)

            if distance[current_node] == inf:
                break

            for neighbour, cost in self.neighbours[current_node]:
                other_route = distance[current_node] + cost

                if other_route < distance[neighbour]:
                    distance[neighbour] = other_route
                    before[neighbour] = current_node
        
        output_path, current_vertex = [], endNode
        
        while before[current_vertex] is not None:
            output_path.insert(0, current_vertex)
            current_vertex = before[current_vertex]
        else:
            if output_path:
                output_path.insert(0, current_vertex)
        # Code end
        return output_path
