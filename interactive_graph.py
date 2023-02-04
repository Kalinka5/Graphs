from netgraph import InteractiveGraph


def create_interactive_graph(graph_data, node_community, size, color_n, labels_n, shapes, edge_labels, edge_color, ax, label_backgrounds):
    g = InteractiveGraph(graph_data,
                         node_layout='community',
                         # if you use node_layout='community', you should clarify node_layout_kwargs:
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

    return g
