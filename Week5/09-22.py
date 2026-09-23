# import networkx as nx
# import matplotlib.pyplot as plt
# G = nx.Graph()
# G.add_edge(1, 2)
# nx.draw_networkx(G)
# plt.show()

# #
# G.add_nodes_from([3, 4])
# nx.draw_networkx(G)
# plt.show()
# G.add_edge(3, 4)
# G.add_edges_from([(2, 3), (4, 1)])
# nx.draw_networkx(G)
# plt.show()

#
print(G.nodes())
print(G.edges())
print(nx.to_dict_of_lists(G))
print(nx.to_numpy_array(G))
print(nx.to_scipy_sparse_array(G))
print(nx.convert_matrix.to_pandas_adjacency(G))

# G.add_edge(1, 3)
# nx.draw_networkx(G)
# plt.show()
# print(G.degree())

# #
# k = nx.fast_gnp_random_graph(1000, 0.01).degree()
# plt.hist(list(dict(k).values()))
# plt.show()

#
# import networkx as nx
# import matplotlib.pyplot as plt
# G = nx.krackhardt_kite_graph()
# nx.draw_networkx(G)
# plt.show()

# #
# print(nx.has_path(G, source = 1, target = 9))
# print(nx.shortest_path(G, source = 1, target = 9))
# print(nx.shortest_path_length(G, source = 1, target = 9))
# print(list(nx.shortest_simple_paths(G, source = 1, target = 9)))

# count = sum(1 for _ in nx.all_simple_paths(G, source = 1, target = 9))
# print(count)

#
# import networkx as nx
# import matplotlib.pyplot as plt
# G = nx.krackhardt_kite_graph()
# nx.draw_networkx(G)
# print("Betweenness: ", nx.betweenness_centrality(G))
# print("\n")
# print("Degree Centrality: ", nx.degree_centrality(G))
# print("\n")
# print("Closeness Centrality: ", nx.closeness_centrality(G))
# print("\n")
# print("Harmonic Centrality: ", nx.harmonic_centrality(G))
# print("\n")
# print("Eigenvector Centrality: ", nx.eigenvector_centrality(G))
# print("\n")
# print("Clustering: ", nx.clustering(G))

# #
# import networkx as nx
# import matplotlib.pyplot as plt
# import community
# import community as community_louvain
# G = nx.powerlaw_cluster_graph(100, 1, 0.4, seed = 100)
# partition = community.best_partition(G)

# for i in set(partition.values()):
#     print("Community ", i, ":", [node for node in partition.keys() if partition[node] == i])
#     members = [node for node in partition.keys() if partition[node] == i]
#     print(members)

# values = [partition.get(node) for node in G.nodes()]
# plt.figure()
# nx.draw(G, pos = nx.fruchterman_reingold_layout(G), cmap = plt.get_cmap("jet"), node_color = values, node_size = 30, with_labels = False)
# plt.title("Community Structure")
# mod_score = community.modularity(partition, G)
# print("Modularity score: ", mod_score)
# plt.show()

#
# import networkx as nx
# import matplotlib.pyplot as plt
# G = nx.krackhardt_kite_graph()
# d = nx.coloring.greedy_color(G)
# print(d)
# nx.draw_networkx(G, node_color = [d[n] for n in sorted(d.keys())])
# plt.show()

#
# import networkx as nx
# import matplotlib.pyplot as plt
# G = nx.DiGraph()
# G.add_edges_from([("A", "B"), ("B", "C"), ("E", "A"), ("C", "A")])
# nx.draw(G, with_labels = True, node_color = "red", node_size = 200)
# plt.show()
# print()
# print()
# plt.show()

#
# import networkx as nx
# import matplotlib.pyplot as plt
# import community
# import community as community_louvain
# G = nx.Graph()
# G.add_edges_from([("A", "B"), ("B", "C"), ("E", "A"), ("C", "A")])
# communities = list(community.greedy_modularity_communities(G))
# num_communities = len(communities)
# print("Number of Communities: ", num_communities)
# plt.show()
# ...

#
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
users = ["Alex", "Sam", "Zaki", "Kate", "Ben"]
friendships = [("Alex", "Ben"), ("Ben", "Zaki"), ("Sam", "Alex"), ("Zaki", "Alex")]
G.add_edges_from(friendships)
nx.draw(G, with_labels = True, node_color = "red", node_size = 2000)
plt.show()
print(dict(G.degree(0)))

#
preds = list(nx.common_neighbors(G, "Sam", "Ben"))
print(preds)

#
max_degree = max(dict(G.degree()).values())
print("Most connected users:")
for node, degree in G.degree():
    if degree == max_degree:
        print(node)

# ...

#
preds = nx.jaccard_coefficient(G, [("Sam", "Ben")])

for u, v, p in preds:
    print(f"({u}, {v}: {p}")

#
import pandas as pd
df = pd.read_csv("Pol.csv")
people = {}

for idx, row in df.iterrows():
    for p in [row['source'], row['target']]:
        if p not in people:
            people[p] = set()
            people[p].add(row['party'])

R = []
D = []
both = []

for p, parties in people.items():
    if parties == {'R'}:
        R.append(p)
    elif parties == {'D'}:
        D.append(p)
    elif parties == {'R', 'D'}:
        both.append(p)

    print("R:", R)
    print("D:", D)
    print("Both:", both)

#