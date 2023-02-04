# Graphs
![Pypi](https://img.shields.io/pypi/v/matplotlib?color=orange&style=plastic)
![Python](https://img.shields.io/pypi/pyversions/matplotlib?color=gree&style=plastic)
![Watchers](https://img.shields.io/github/watchers/Kalinka5/Graphs?style=social)
![Stars](https://img.shields.io/github/stars/Kalinka5/Graphs?style=social)

*The main idea of this program is creation* **3 different graphs**. In this program I use [networkx](https://networkx.org/documentation/stable/tutorial.html) and [netgraph](https://github.com/paulbrodersen/netgraph) to create directed graphs and interact with them. Next you will see:
+ *how to read CSV files by keys of dictionary*;
+ *how to create usual* **Graph**;
+ *how to move nodes in an* **Interactive Graph**;
+ *how to add more information to an* **Editable Graph**.
___

## *Usage*
To begin with, you should create csv file with graph data. This file should contains *nodes*, *node's size*, *node's color*, *edges* etc.\
I use [Pandas library](https://pypi.org/project/pandas/) to illustrate the table, but you don't need install this library to interact with this program:

![Table](https://user-images.githubusercontent.com/106172806/216014331-0534c828-a491-4e46-8a0f-caf09bb7c0eb.jpg)

Also, you should install [networkx](https://pypi.org/project/networkx/), [netgraph](https://pypi.org/project/netgraph/) and [matplotlib](https://pypi.org/project/matplotlib/) packages.
___

## *Example*
First of all, open CSV file and read data like dictionary:
```python
with open("graph_data.csv") as graph_data:
    reader = csv.DictReader(graph_data)
```
Having created the variables first, we assign them the values from the table.
```python
# All variables to draw a graph
edges = []
size, color_n, labels_n, shapes, edge_labels, edge_color, node_community, label_backgrounds = ({} for i in range(8))
```

```python
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
```

And since our last row doesn't contain edge information we should make conditional to ignore empty values:
```python
if row["first_node"] != "":
    # Add edges to variable, for example: {("0", "1"), ("0", "2"),...}
    edges.append((row["first_node"], row["second_node"]))

    # Add edge labels to variable, for example: {("0", "1"): "operate", ("0", "2"): "operate",...}
    edge_labels[(row["first_node"], row["second_node"])] = row["edge_label"]

    # Add edge color to variable, for example: {("0", "1"): "red",... ("1", "5"): "green",...}
    edge_color[(row["first_node"], row["second_node"])] = row["edge_color"]
```
Finally, create directed graph and save it in variable graph_data:
```python
# Create DiGraph
graph_data = nx.DiGraph(edges)
```

### *Graph*
First, usual graph. To create this kind of graph, I will use custom position of our nodes. Where keys are nodes and values are x and y axis:
```python
pos = {"0": (0, 1), "1": (-1, 0), "2": (-0.5, 0), "3": (0.5, 0), "4": (1, 0), "5": (-2.5, -1), "6": (-2, -1),
       "7": (-1.5, -1), "8": (-1, -1), "9": (-0.5, -1), "10": (0, -1), "11": (0.5, -1), "12": (1, -1),
       "13": (1.5, -1), "14": (2, -1)}
```
But you can use another different node_layot, like "dot", "circular" and "community". Next graphs will use some of them.

Then, create our graph with all options:
```python
g = create_graph(graph_data, pos, size, color_n, labels_n, shapes, edge_labels, edge_color, ax, label_backgrounds)
```
For the final result, we will change node's background color and node's label size.
```python
# Create background color to our node labels
for node, color in label_backgrounds.items():
    g.node_label_artists[node].set_backgroundcolor(color)

# We can control font size of our node labels
for node, label in g.node_label_artists.items():
    fontsize = label.get_fontsize()
    label.set_fontsize(fontsize * 5)
```

As a result we will get graph like this one:
![graph](https://user-images.githubusercontent.com/106172806/216035828-dcf1201d-a9f1-4774-9ff3-f96d828d1bb2.png)
___

### *Interctive Graph*
Let's move on to the second graph. To create Interactive Graph I use "community" node_layot.\
In our CSV file we have column "node_community" where write groups (1, 2 or 3).

In the first group locate only "0" node. Second group has 4 nodes and third group contains 10 nodes.

Then, call the function create_interactive_graph(parameters), where node_layout = "community":
```python
g = InteractiveGraph(graph_data,
                     node_layout='community',
                     # if you use node_layout='community', you should clarify node_layout_kwargs:
                     node_layout_kwargs=dict(node_to_community=node_community),
                     ... # rest peace of code the same
```
Node's background color and node's label size automatically change too.

As we create Interactive graph, unfortunately It doesn't look like as we need. Since we used community position, nodes locates by different groups.
So, let's move our nodes to great layot:

![interactive_graph](https://user-images.githubusercontent.com/106172806/216788092-5c8fb3d6-6adf-4062-a5b0-300cc3fd6ab8.gif)

As a result you will get graph like this:
![interactive_graph](https://user-images.githubusercontent.com/106172806/216050830-59d69cd5-7c38-4037-a574-99de6c146bc7.png)
___

### *Editable Graph*
The third one is a graph where we can edit any parameters, add new nodes and edges, create an annotation and so on.

This time we will use "dot" node layot, which create serial chain of our nodes.

Code of Editable Graph looks like this one: 
```python
def create_editable_graph(graph_data, size, color_n, labels_n, shapes, edge_labels, edge_color, ax, label_backgrounds):
g = EditableGraph(graph_data,
                  node_layout='dot',
                  ... # rest peace of code the same
```

After creation Editable graph, let's update it. We will add some descriptions:

![editable_graph](https://user-images.githubusercontent.com/106172806/216788118-74b701cb-c297-42a7-aa5c-32675c0e288b.gif)

Furthermore, you can add new nodes and edges to our drawing, but as for this graph we don't need it. Also, you can read about editing graph in this [link](https://github.com/paulbrodersen/netgraph), where in README file fully explained it.

At the end, you can get this graph:
![editable_graph](https://user-images.githubusercontent.com/106172806/216053747-97d11a1b-4069-44ee-a340-b424b3c57982.png)

___
