import matplotlib.pyplot as plt
import networkx as nx
from netgraph import InteractiveGraph
import csv

if __name__ == '__main__':

    edges = []
    size, color_n, labels_n, shapes, edge_labels, edge_color, node_community, label_backgrounds = ({} for i in range(8))

    with open("graph_data.csv") as graph_data:
        reader = csv.DictReader(graph_data)
        for row in reader:
            size[row["node"]] = int(row["node_size"])
            color_n[row["node"]] = row["node_color"]
            labels_n[row["node"]] = row["node_label"]
            shapes[row["node"]] = row["node_shape"]
            node_community[row["node"]] = row["node_community"]
            label_backgrounds[row["node"]] = row["background_color"]
            if row["first_node"] != "":
                edges.append((row["first_node"], row["second_node"]))
                edge_labels[(row["first_node"], row["second_node"])] = row["edge_label"]
                edge_color[(row["first_node"], row["second_node"])] = row["edge_color"]

        # I don't know what it is
        fig, ax = plt.subplots()

        # Create DiGraph
        graph_data = nx.DiGraph(edges)

        # Create position of each element on sheet by X-axis and Y-axis (X, Y)
        # pos = {0: (0, 0)}
        # x = -3
        # y = -2.5
        # for i in variables:
        #     if 0 < i <= len(gmails):
        #         pos[i] = (x, y)
        #         y += 0.5
        #     elif i > len(gmails):
        #         if y > 2.5:
        #             y = 2.5
        #             x = 3
        #         pos[i] = (x, y)
        #         y -= 0.5

        # There using InteractiveGraph, but you can also use EditableGraph, Graph
        g = InteractiveGraph(graph_data,
                             node_layout='community',  # or you can use pos - X, Y axis
                             # if you use node_layout='community'
                             node_layout_kwargs=dict(node_to_community=node_community),
                             node_size=size,
                             node_color=color_n,
                             node_labels=labels_n,
                             node_label_fontdict={'backgroundcolor': 'lightgray'},
                             node_shape=shapes,
                             edge_labels=edge_labels,
                             edge_layout='straight',  # or you can use 'straight', 'curved' layout
                             edge_label_fontdict=dict(fontweight='bold'),
                             edge_color=edge_color,
                             edge_alpha=1,  # transparency from 0 to 1
                             arrows=True,  # draw edges with arrow heads.
                             ax=ax
                             )

        # Create background color to our node labels
        for node, color in label_backgrounds.items():
            g.node_label_artists[node].set_backgroundcolor(color)

        # We can control font size of our node labels
        for node, label in g.node_label_artists.items():
            fontsize = label.get_fontsize()
            label.set_fontsize(fontsize * 5)

        # Show our Graph
        plt.show()

        # You can use help cheatsheet each of graph: EditableGraph, Graph, InteractiveGraph
        # help(InteractiveGraph)
