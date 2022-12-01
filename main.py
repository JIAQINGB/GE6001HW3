# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import networkx as nx

# importing the matplotlib library for plotting the graph
import matplotlib.pyplot as plt


def cal_graph_info(n, p):
    print("The NODE NUMBER IS: ", n, " and p : ", p)
    G = nx.erdos_renyi_graph(n, p)
    print("number of edge: ", G.number_of_edges())
    dg = nx.degree(G)
    dl = []
    dl = [val for (node, val) in dg]
    print("最大度：", max(dl))
    print("最小度：", min(dl))
    print("平均聚类 : ", nx.average_clustering(G))
    cyc = nx.cycle_basis(G)
    if not cyc:
        print("无圈")
    else:
        print("有圈")
    print("是否连通：", nx.is_connected(G))
    if nx.is_connected(G):
        print("平均距离 : ", nx.average_shortest_path_length(G))
    lenlist = []
    for sub in nx.connected_components(G):
        lenlist.append(len(sub))
    print("最大连通分支节点个数：", max(lenlist))


if __name__ == "__main__":
    node_list = [100, 1000, 2000]
    p_list = [0.00001, 0.0001, 0.001, 0.01]
    for i in node_list:
        for j in p_list:
            cal_graph_info(i, j)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
