import networkx as x, os, pickle

# tdir = "../../social/data/facebook/"
# fs = os.listdir(tdir)
# 
# def readGml(gfile):
#         with open(gfile) as f:
#             lines = f.readlines()
#         friendship_network = x.readwrite.gml.parse_gml_lines(lines, "id", None)
#         return friendship_network
# 
# nets = []
# for f in fs:
#     if f.endswith(".gml"):
#         nets.append(readGml(tdir+f))
#         print(f)
# 
# pickle.dump(nets,open('../data/nets.pickle', 'wb'),-1)

# get number of nodes, edges, top 50 closeness and top 50 betweenness

nets = pickle.load(open('../data/nets.pickle', 'rb'))

data = []
for net in nets:
    nnodes = net.number_of_nodes()
    nedges = net.number_of_edges()

    cc = x.closeness_centrality(net)
    cc_ = sorted(cc.items(), key=lambda x: x[1])
    s1 = set([i[0] for i in cc_[-50:]])

    bc = x.betweenness_centrality(net)
    bc_ = sorted(bc.items(), key=lambda x: x[1])
    s2 = set([i[0] for i in bc_[-50:]])

    n_both = len(s1 & s2)

    data.append([nnodes, nedges, n_both])
    print([nnodes, nedges, n_both, cc_, bc_])


pickle.dump(data,open('../data/nets2.pickle', 'wb'),-1)
data = pickle.load(open('../data/nets2.pickle', 'rb'))
