graph_theory = """
Introduction to Graphs

	Graphs are the perfect data structure for modeling networks, which make them an indispensable piece of your data structure toolkit.
	 They’re composed of nodes, or vertices, which hold data, and edges, which are a connection between two vertices. A single node is a vertex.
	Consider a map of the area where you live. As a graph, we could model bus stops as vertices, with bus routes between stops functioning as the edges.
	What about the internet? Web pages can be vertices, and the hyperlinks which connect them are edges.
	Real-world relationships modeled as graphs are numerous, making them an essential concept to master.

Introduction to Graphs

	Graphs are the perfect data structure for modeling networks, which make them an indispensable piece of your data structure toolkit.
	 They’re composed of nodes, or vertices, which hold data, and edges, which are a connection between two vertices. A single node is a vertex.
	Consider a map of the area where you live. As a graph, we could model bus stops as vertices, with bus routes between stops functioning as the edges.
	What about the internet? Web pages can be vertices, and the hyperlinks which connect them are edges.
	Real-world relationships modeled as graphs are numerous, making them an essential concept to master.

Directed Graphs

	Imagine you’re a superhero escaping a villain’s lair. As you move from perilous room to perilous room,
	 the doors close immediately behind you, barring any return.
	For this dramatic example, we need a directed graph, where edges restrict the direction of movement between vertices.
	We can move from spikes to lasers, but not from lasers to spikes. This differs from earlier examples when every edge was bi-directional.
	Note the path spikes to lasers to piranhas to spikes. This path is a cycle, because it ends on the vertex where it began: spikes.

Reviewing Key Terms

	Graphs are an essential data structure in computer science for modeling networks. Let’s review some key terms:

	    vertex: A node in a graph.
	    edge: A connection between two vertices.
	    adjacent: When an edge exists between vertices.
	    path: A sequence of one or more edges between vertices.
	    disconnected: Graph where at least two vertices have no path connecting them.
	    weighted: Graph where edges have an associated cost.
	    directed: Graph where travel between vertices can be restricted to a single direction.
	    cycle: A path which begins and ends at the same vertex.
	    adjacency matrix: Graph representation where vertices are both the rows and the columns. Each cell represents a possible edge.
	    adjacency list: Graph representation where each vertex has a list of all the vertices it shares an edge with.
	


Let’s detail the functionality we require from classes:

    Vertex stores some data.
    Vertex stores the edges to connected vertices and their weight.
    Vertex can add a new edge to its collection.
    Graph stores all the vertices.
    Graph knows if it is directed or undirected.
    Graph can add a new vertex to its collection.
    Graph can add a new edge between stored vertices.
    Graph can tell whether a path exists between stored vertices.

"""



class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex):
    print("Adding edge to ", vertex)
    self.edges[vertex] = True
    
  def get_edges(self):
    return list(self.edges.keys())
  
  
grand_central = Vertex('Grand Central Station')
forty_second_street = Vertex('42nd Street Station')

print(grand_central.get_edges())

# call .add_edge() here
grand_central.add_edge(forty_second_street.value)

print(grand_central.get_edges())




# Basic Graph


class Graph:
  def __init__(self, directed=False):
    self.directed = directed
    self.graph_dict = {}
  
  def add_vertex(self, vertex):
    print("Adding ", vertex.value)
    self.graph_dict[vertex.value] = vertex


grand_central = Vertex("Grand Central Station")

# Uncomment this code after you've defined Graph
railway = Graph()

# Uncomment these lines after you've completed .add_vertex()
print(railway.graph_dict)
railway.add_vertex(grand_central)
print(railway.graph_dict)





# example of complete Graph
class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight = 0):
    self.edges[vertex] = weight

  def get_edges(self):
    return list(self.edges.keys())


class Graph:
  def __init__(self, directed = False):
    self.graph_dict = {}
    self.directed = directed

  def add_vertex(self, vertex):
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight = 0):
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    if not self.directed:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

  def find_path(self, start_vertex, end_vertex):
    start = [start_vertex]
    seen = {}
    # vertices we've already visited
    while len(start) > 0:
      current_vertex = start.pop(0)
      # Checkpoint 2, replace these comments:
      seen[current_vertex] = True
      # Update the `seen` variable
      # now that we've visited current_vertex
      print("Visiting " + current_vertex)
      if current_vertex == end_vertex:
        return True
      else:
        vertex = self.graph_dict[current_vertex]
        next_vertices = vertex.get_edges()
        
        # Filter next_vertices so it only
        # includes vertices NOT IN seen
        
        # Checkpoint 3, uncomment and replace the question marks:
        next_vertices = [vertex for vertex in next_vertices if vertex not in seen]
        start.extend(next_vertices)
        
    return False


railway = Graph()

callan = Vertex('callan')
peel = Vertex('peel')
ulfstead = Vertex('ulfstead')
harwick = Vertex('harwick')

railway.add_vertex(callan)
railway.add_vertex(peel)
railway.add_vertex(harwick)
railway.add_vertex(ulfstead)

railway.add_edge(peel, harwick)
railway.add_edge(harwick, callan)
railway.add_edge(callan, peel)

# Uncomment the code below when you're done refactoring!

peel_to_ulfstead_path_exists = railway.find_path('peel', 'ulfstead')
harwick_to_peel_path_exists = railway.find_path('harwick', 'peel')

print("A path exists between peel and ulfstead:")
print(peel_to_ulfstead_path_exists)
print("A path exists between harwick and peel:")
print(harwick_to_peel_path_exists)

