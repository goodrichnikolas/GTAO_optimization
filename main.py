'''
This script will find the most efficient path between nodes in GTA Online
'''

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Create the graph

class Business:
    def __init__(self, name, type_, location, coords, purchase_cost):
        self.name = name
        self.type_ = type_
        self.location = location
        self.coords = coords
        self.x_coord = coords[0]
        self.y_coord = coords[1]
        self.purchase_cost = purchase_cost

    def __str__(self):
        return self.type_

    def __repr__(self):
        return self.type_
    
# Assume the edge weight is the Euclidean distance between nodes
def calculate_distance(business1, business2):
    x_distance = business1.x_coord - business2.x_coord
    y_distance = business1.y_coord - business2.y_coord
    return np.sqrt(x_distance**2 + y_distance**2)


x_min = 0
x_max = 118
y_min = 0
y_max = 160

#Create references to businesses

weed_paleto = Business('weed_paleto', 'Weed Farm', 'Paleto Bay', (58, 24), 805200)
weed_grapeseed = Business('weed_grapeseed', 'Weed Farm', 'Grapeseed', (91, 51), 715000)
weed_vinewood = Business('weed_vinewood', 'Weed Farm', 'Vinewood', (55, 107), 1358500)
weed_port= Business('weed_port', 'Weed Farm', 'Port of South Los Santos', (54, 141), 1072500)

forgery_paleto = Business('forgery_paleto', 'Forgery Office', 'Paleto Bay', (51, 26), 732000)
forgery_grapeseed = Business('forgery_grapeseed', 'Forgery Office', 'Grapeseed', (74, 44), 650000)
forgery_downtown = Business('forgery_downtown', 'Forgery Office', 'Downtown Vinewood', (57, 117), 1235000)
forgery_port = Business('forgery_port', 'Forgery Office', 'Port of South Los Santos', (48, 145), 975000)

counterfeit_paleto = Business('counterfeit_paleto', 'Counterfeit Cash Factory', 'Paleto Bay', (47, 28), 951600)
counterfeit_harmony = Business('counterfeit_harmony', 'Counterfeit Cash Factory', 'Harmony', (60, 72), 845000)
counterfeit_vespucci = Business('counterfeit_vespucci', 'Counterfeit Cash Factory', 'Vespucci Canals', (37, 127), 1600000)
counterfeit_port = Business('counterfeit_port', 'Counterfeit Cash Factory', 'Port of South Los Santos', (61, 145), 1265000)

meth_paleto = Business('meth_paleto', 'Meth Lab', 'Paleto Bay', (54, 26), 1024000)
meth_harmony = Business('meth_harmony', 'Meth Lab', 'Harmony', (55, 76), 910000)
meth_east_los_santos = Business('meth_east_los_santos', 'Meth Lab', 'East Los Santos', (71, 130), 1720000)
meth_port = Business('meth_port', 'Meth Lab', 'Port of South Los Santos', (68, 150), 1360000)

cocaine_paleto = Business('cocaine_paleto', 'Cocaine Lockup', 'Paleto Bay', (53, 24), 1098000)
cocaine_alamo = Business('cocaine_alamo', 'Cocaine Lockup', 'Alamo Sea', (57, 62), 975000)
cocaine_morningwood = Business('cocaine_morningwood', 'Cocaine Lockup', 'Morningwood', (32, 113), 1850000)
cocaine_port = Business('cocaine_port', 'Cocaine Lockup', 'Port of South Los Santos', (49, 143), 1462500)


#Create lists of businesses

weed_list = [weed_paleto, weed_grapeseed, weed_vinewood, weed_port]
forgery_list = [forgery_paleto, forgery_grapeseed, forgery_downtown, forgery_port]
counterfeit_list = [counterfeit_paleto, counterfeit_harmony, counterfeit_vespucci, counterfeit_port]
meth_list = [meth_paleto, meth_harmony, meth_east_los_santos, meth_port]
cocaine_list = [cocaine_paleto, cocaine_alamo, cocaine_morningwood, cocaine_port]

# Create a graph
G = nx.Graph()

# Add nodes to the graph
all_businesses = weed_list + forgery_list + counterfeit_list + meth_list + cocaine_list
for business in all_businesses:
    G.add_node(business)

# Add edges to the graph (assuming it's fully connected)
for business1 in all_businesses:
    for business2 in all_businesses:
        if business1 != business2:  # Exclude self-loops
            distance = calculate_distance(business1, business2)
            G.add_edge(business1, business2, weight=distance)

# Approximate solution for the Travelling Salesman Problem
cycle = nx.approximation.greedy_tsp(G, source=weed_paleto, weight='weight')

print("Approximate shortest cycle:", cycle)

# Now filter the cycle to ensure that only one business from each type is visited
filtered_cycle = []
visited_types = set()
for node in cycle:
    if node.type_ not in visited_types:
        filtered_cycle.append(node)
        visited_types.add(node.type_)

print("Filtered cycle:", [business.name for business in filtered_cycle])
