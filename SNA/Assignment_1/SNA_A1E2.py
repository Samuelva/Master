"""
Run: python3 SNA_A1E2.py medium.in medium
Required packages:
python3-tk
"""
import sys
import networkx as nx
from collections import Counter, OrderedDict
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline

def main(network_data, network_name):
    # large = nx.read_adjlist("/media/samuel/Danker/School_data/SNA/large.in", create_using=nx.DiGraph())
    network = nx.read_edgelist(network_data, create_using=nx.DiGraph())
    # medium_graph = nx.read_adjlist("/media/samuel/Danker/School_data/SNA/medium.in")
    # large.number_of_nodes()
    # large.number_of_edges()
    in_degree_counts = Counter(dict(network.in_degree()).values())
    out_degree_counts = Counter(dict(network.out_degree()).values())

    # connected_components(network)

    # plot_degree(in_degree_counts, network_name, "in")
    # plot_degree(out_degree_counts, network_name, "out")
    distances(network)

def distances(network):
    shortest_distances = nx.all_pairs_shortest_path(network)
    distance_distribution = {}

    for node in shortest_distances:
        for paths in shortest_distances[node].values():
            path_length = len(paths)-1
            if path_length not in distance_distribution:
                distance_distribution[path_length] = 1
            else:
                distance_distribution[path_length] += 1
    print(distance_distribution)
    del distance_distribution[0]
    distribution_plot(list(distance_distribution.keys()), list(distance_distribution.values()))
                

def connected_components(network):
    scc = nx.number_strongly_connected_components(network)
    wcc = nx.number_weakly_connected_components(network)

    print("# of strongly connected components: " + str(scc))
    print("# of weakly connected components: " + str(wcc))


def plot_degree1(degree, network, type):
    number_of_links = sorted(list(degree.keys()))
    frequency = list(degree.values())
    # x_axis = np.arange(len(number_of_links))
    distribution_plot()


def distribution_plot(x, y):
    plt.bar(x, y)
    # plt.yticks(y, number_of_links, rotation="vertical")
    plt.xlabel("Number of links between nodes")
    plt.ylabel("Frequency")

    # if type == "in":
    #     plt.title("Indegree distribution of " + network)
    # elif type == "out":
    #     plt.title("Outdegree distribution of " + network)
    plt.show()    

def plot_degree(degree, network, type):
    number_of_links = sorted(list(degree.keys()))
    frequency = list(degree.values())
    x_axis = np.arange(len(number_of_links))

    f, (axis1, axis2) = plt.subplots(2, 1, sharex=True)
    axis1.grid(axis="y", color="black", linestyle="--", linewidth=1, alpha=.25)
    axis2.grid(axis="y", color="black", linestyle="--", linewidth=1, alpha=.25)

    axis1.bar(x_axis, frequency)
    axis2.bar(x_axis, frequency)

    # smooth_x_axis = np.linspace(x_axis.min(), x_axis.max(), 500)
    # smooth_frequency = spline(x_axis, frequency, smooth_x_axis)
    # smooth_frequency = np.linspace(min(frequency), max(frequency), 500)

    axis1.plot(x_axis, frequency, "--", color="#aec7e8")
    axis2.plot(x_axis, frequency, "--", color="#aec7e8")
    
    axis1.set_ylim(1800, 2000)
    axis2.set_ylim(0, 60)

    axis1.spines["top"].set_visible(False)
    axis1.spines["bottom"].set_visible(False)
    axis1.spines["right"].set_visible(False)
    axis2.spines["top"].set_visible(False)
    axis2.spines["right"].set_visible(False)

    axis1.tick_params(bottom="off", labelbottom="off")

    plt.xticks(x_axis, number_of_links, rotation="vertical")
    plt.xlabel("Number of links between nodes")
    plt.ylabel("Frequency")

    # if type == "in":
    #     plt.title("Indegree distribution of " + network)
    # elif type == "out":
    #     plt.title("Outdegree distribution of " + network)
    plt.show()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

"""
for x in distance:
    for y in distance[x].values():
        if len(y)-1 not in testdict:
            testdict[len(y)-1] = 1
        else:
            testdict[len(y)-1] += 1
"""