import xmlrpclib, time, random

# Number of dimensions for hypercube
dim = 6

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2';
server = xmlrpclib.Server(server_url);
G = server.ubigraph

G.clear()

 #While we are building the graph, make everything invisible.
G.set_vertex_style_attribute(0, "visible", "false")
G.set_edge_style_attribute(0, "visible", "false")

 #Default vertex styles
G.set_vertex_style_attribute(0, "shape", "sphere")
G.set_vertex_style_attribute(0, "color", "#F4FF85")
G.set_vertex_style_attribute(0, "size", "0.25")


class stru:
    def __init__(self):
        self.x = 0
        self.y = 0

vertexCount = 10;

for i in xrange(0,vertexCount):
  G.new_vertex_w_id(i)

for i in xrange(0,vertexCount):
    for j in xrange(i+1, vertexCount):
      G.new_edge(i, j)

 #While we are building the graph, make everything invisible.
G.set_vertex_style_attribute(0, "visible", "true")
G.set_edge_style_attribute(0, "visible", "true")

