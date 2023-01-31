import matplotlib.pyplot as plt
import networkx as nx
import csv
from interactive_graph import create_interactive_graph
from graph import create_graph
from editable_graph import create_editable_graph

if __name__ == '__main__':

    # All variables to draw a graph
    edges = []
    size, color_n, labels_n, shapes, edge_labels, edge_color, node_community, label_backgrounds = ({} for i in range(8))

    with open("graph_data.csv") as graph_data:
        reader = csv.DictReader(graph_data)
        for row in reader:
            # Add node size to variable, for example: {"0": 15, "1": 10,...}
            size[row["node"]] = int(row["node_size"])

            # Add node color to variable, for example: {"0": "red", "1": "green",...}
            color_n[row["node"]] = row["node_color"]

            # Add node labels to variable, for example: {"0": "Chief Technology Officer",...}
            labels_n[row["node"]] = row["node_label"]

            # Add node shapes to variable, for example: {"0": "p", "1": "s",...}
            shapes[row["node"]] = row["node_shape"]

            # Add node groups of community to node layout, for example: {"0": "0", "1": "1", "2": "1",..., "5": "3",...}
            node_community[row["node"]] = row["node_community"]

            # Add node label background color to variable, for example: {"0": "salmon", "1": "lightgreen",...}
            label_backgrounds[row["node"]] = row["background_color"]

            if row["first_node"] != "":

                # Add edges to variable, for example: {("0", "1"), ("0", "2"),...}
                edges.append((row["first_node"], row["second_node"]))

                # Add edge labels to variable, for example: {("0", "1"): "operate", ("0", "2"): "operate",...}
                edge_labels[(row["first_node"], row["second_node"])] = row["edge_label"]
                
                # Add edge color to variable, for example: {("0", "1"): "red",... ("1", "5"): "green",...}
                edge_color[(row["first_node"], row["second_node"])] = row["edge_color"]

        # I don't know what it is
        # fig, (ax1, ax2) = plt.subplots(1, 2)
        fig, ax = plt.subplots()

        # Create DiGraph
        graph_data = nx.DiGraph(edges)

        # Create Interactive_Graph
        # ig = create_interactive_graph(graph_data, node_community, size, color_n, labels_n, shapes, edge_labels, edge_color, ax, label_backgrounds)

        # Create Graph
        # Create position of each element on sheet by X-axis and Y-axis (X, Y)
        # pos = {"0": (0, 1), "1": (-1, 0), "2": (-0.5, 0), "3": (0.5, 0), "4": (1, 0), "5": (-2.5, -1), "6": (-2, -1),
        #        "7": (-1.5, -1), "8": (-1, -1), "9": (-0.5, -1), "10": (0, -1), "11": (0.5, -1), "12": (1, -1),
        #        "13": (1.5, -1), "14": (2, -1)}
        # g = create_graph(graph_data, pos, size, color_n, labels_n, shapes, edge_labels, edge_color, ax, label_backgrounds)

        # Create EditableGraph
        eg = create_editable_graph(graph_data, node_community, size, color_n, labels_n, shapes, edge_labels, edge_color, ax, label_backgrounds)

        # Show our Graph
        plt.show()
