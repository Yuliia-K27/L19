import pandas as pd

# Load data from the Google Drive link
url = 'https://drive.google.com/file/d/1Hk8G9sCE9gRjLw6c-aiaClaA4FFCUYYh/view?usp=sharing'
file_id = url.split('/')[-2]
dwn_url = 'https://drive.google.com/uc?id=' + file_id
data = pd.read_csv(dwn_url)

# Create a list of cities and distances
cities = []
for i in range(len(data)):
    city1 = data.iloc[i][0]
    city2 = data.iloc[i][1]
    km = data.iloc[i][2]
    cities.append([city1, city2, km])

    
    
    
import networkx as nx
import matplotlib.pyplot as plt

# Create a new graph
G = nx.Graph()

# Add nodes to the graph (cities)
cities_list = []
for city1, city2, km in cities:
    cities_list.append(city1)
    cities_list.append(city2)
cities_set = set(cities_list)
G.add_nodes_from(cities_set)

# Add edges to the graph (distances)
for city1, city2, km in cities:
    G.add_edge(city1, city2, weight=km)

# Draw the graph
pos = nx.spring_layout(G, seed=42) # Position nodes using the Fruchterman-Reingold force-directed algorithm
labels = nx.get_edge_attributes(G,'weight') # Get edge weights as labels
nx.draw_networkx_nodes(G, pos, node_size=100, node_color='lightblue')
nx.draw_networkx_edges(G, pos, width=1, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8, font_family='sans-serif')
plt.axis('off')
plt.show()


