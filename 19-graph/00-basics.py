# Graph
# G = (V, E)
# V = {v1, v2, v3, v4, v5}
# E = {(v1,v2),(v2,v4),(v1,v3),(v3,v4),(v3,v5),(v4,v5)}

#  UnDirected Graph
#  (v1)------(v3)
#   |         |   \
#   |         |    (v5)  
#   |         |   /
#  (v2)------(v4)
#   degree of v1 = 2
#  sum of degrees = 2 * |E|
#  max possible edges = (|V| * (|V| - 1)) / 2


# Directed Graph
#  (v1)------->(v3)
#   |              \
#   |               V
#   |              (v5)
#   |               /
#   V              V
#  (v2)------->(v4)

# indegree of v1 - 0
# outdegree of v1 - 2
# max possible edges = |V| * (|V| - 1)
# sum of indegrees = |E|
# sum of outdegrees = |E|
