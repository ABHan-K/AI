import numpy as np
import AI_ImportingNetworkData
import os
import re
import xlrd
import xlwt
import matplotlib.pyplot as plt
import networkx as nx


G = nx.Graph()  # 创立一个空的无向图
nodes_num = 36  # 节点个数
nodes = list(range(36))
# nodes_name = []
# for i in range(nodes_num):
#     nodes_name.append(i + 1)
ai = AI_ImportingNetworkData.Read(r'F:\360MoveData\Users\DELL\Desktop\数据.xlsx')
ai.read_line()
G.add_nodes_from(nodes)
coordinates = np.zeros((36, 2))  # 设置坐标
i = 1
while i < ai.rows0:
    coordinates[i - 1, 0] = ai.bus_data[i, 2]
    coordinates[i - 1, 1] = ai.bus_data[i, 3]
    i += 1
vnode = np.array(coordinates)
npos = dict(zip(nodes, vnode))  # 获取节点与坐标之间的映射关系，用字典表示
nlabels = dict(zip(nodes, nodes))  # 标志字典，构建节点与标识点之间的关系

# i = 1
# while i < ai.rows0:
#     if ai.bus_data[i, 2] != 0 and ai.bus_data[i, 3] != 0:
#         nodes[i - 1, 0] = ai.bus_data[i, 2]
#         nodes[i - 1, 1] = ai.bus_data[i, 3]
#         position = {i: (nodes[i - 1, 0], nodes[i - 1, 1])}
#     else:
#         position = {i: (np.random.randint(0, 100), np.random.randint(0, 100))}
#     i += 1

# edges = []
# for idx in range(point_num - 1):
#     edges.append((idx, idx + 1))
# edges.append((point_num - 1, 0))
# G.add_edges_from(edges)

#nx.draw_networkx(G, pos=position)
nx.draw_networkx_nodes(G, npos, node_size=50, node_color="#6CB6FF")  # 绘制节点
plt.show()



