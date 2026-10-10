# Homework_3
# Dr. Afrand Agah

# Steve Handy
# 0796861

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

file_path = Path(__file__).with_name("facebook_combined.txt")

graph = nx.read_edgelist(file_path, nodetype = int)

print("Total nodes:", graph.number_of_nodes())
print("Total edges:", graph.number_of_edges())

degree_centrality = nx.degree_centrality(graph)
eigenvector_centrality = nx.eigenvector_centrality(graph, max_iter = 1000)

print("\nTop 5 by degree centrality:")
for node, score in sorted(
    degree_centrality.items(),
    key = lambda item: item[1],
    reverse = True
)[:5]:
    print(node, score)

print("\nTop 5 by eigenvector centrality:")
for node, score in sorted(
    eigenvector_centrality.items(),
    key = lambda item: item[1],
    reverse = True
)[:5]:
    print(node, score)

plt.hist(degree_centrality.values(), bins = 30)
plt.title("Degree Centrality Distribution")
plt.xlabel("Degree centrality")
plt.ylabel("Number of nodes")
plt.show()

plt.hist(eigenvector_centrality.values(), bins = 30)
plt.title("Eigenvector Centrality Distribution")
plt.xlabel("Eigenvector centrality")
plt.ylabel("Number of nodes")
plt.show()

# Why might a node have a high degree but low eigenvector centrality?
#     A node could have many connections with a low influence. In other words, high quantity low quality.