import networkx as nx
import graphviz as gv

class Graph(nx.Graph):
    def __init__(self, start=None):
        super().__init__(start)

    # here are some of the public methods to implement
    
    def neighbors(self, v):
        return list(self.adj[v])
    
    def vertices(self):
        return self.nodes()
    
    #edges()

    def __len__(self):
        return self.number_of_nodes()
    
    def add_vertex(self,a):
        return self.add_node(a)
    
    #add_edge(v1, v2)
    
    def remove_vertex(self, v):
        return self.remove_node(v)

    #remove_edge(v1, v2)

    def get_vertex_value(self, v):
        return self.nodes[v]

    def set_vertex_value(self, v, x):
        self.nodes[v]["location"] = x


class WeightedGraph(Graph):
    def __init__(self):
        super().__init__()

    def set_weight(self, a, b, w):
        self[a][b]["weight"] = w

    def get_weight(self, a, b):
        return self[a][b]["weight"]
    
    	# etc etc
    	# check the lab assignment for details

#shortest_path(graph, source=None, target=None, weight=None, method='dijkstra')

def costs2attributes(G, cost, attr="weight"):
    for a, b in G.edges():
        G[a][b][attr] = cost(a, b)

def dijkstra(graph, source, cost=lambda u,v: 1):
    dict = {}
    costs2attributes(graph, cost)
    for key in nx.shortest_path(graph, source, weight="weight"):
        dict.setdefault(key, {"path": nx.shortest_path(graph, source, weight="weight")[key]})
    return dict

def visualize(graph, view="dot", name = "mygraph", nodecolors=None):
    dot = gv.Graph()
    [dot.node(str(a)) for a in graph.vertices()]
    [dot.edge(str(a), str(b)) for a, b in graph.edges()]
    dot.render("_graph.gv", view = True)

def view_shortest(G, source, target, cost=lambda u,v: 1):
    path = dijkstra(G, source, cost)[target]['path']
    print(path)
    colormap = {str(v): 'orange' for v in path}
    print(colormap)
    visualize(G, view='view', nodecolors=colormap)

def demo():
    G = Graph([(1,2),(1,3),(1,4),(3,4),(3,5),(3,6),(3,7),(6,7)])
    view_shortest(G, 2, 6)

if __name__ == '__main__':
    demo()



g = WeightedGraph()
g.add_vertex(1)
g.add_vertex(5)
g.add_edge(1,5)
print(g.vertices())
print(g.edges())
g.remove_edge(1,5)
print(g.edges())
g.add_edge(1,5)
g.add_vertex(7)
g.add_vertex(9)
g.add_edge(5,9)
g.add_edge(9,7)
print(g.neighbors(9))
g.remove_vertex(5)
print(g.vertices())
print(g.neighbors(9))
print(g.__len__())
g.set_vertex_value(9, 5)
print(g.get_vertex_value(9))
g.get_vertex_value(9)
g.add_edge(7, 9)
g.set_weight(9, 7, 2)
g.add_vertex(3)
g.add_edge(1, 9)
g.set_weight(1, 9, 5)
g.add_edge(7, 3)
g.set_weight(7, 3, 1)
g.add_edge(1, 3)
g.set_weight(1, 3, 69)


print(g.get_weight(7, 9))
print(g.edges())

print(g.vertices())
print(nx.shortest_path(g, source = 1, weight = "weight"))

#print(g.costs2attributes(lambda u,v: 1))

costs2attributes(g, cost=lambda u,v: 1)
print(g.get_weight(7, 9))
print(g.get_weight(7, 3))
print(g.get_weight(3, 1))
print(g.get_weight(1, 9))
print(dijkstra(g, 1))

