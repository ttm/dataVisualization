import networkx as x, pylab as p, os, pickle

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

# nets = pickle.load(open('../data/nets.pickle', 'rb'))
# 
# data = []
# for net in nets:
#     nnodes = net.number_of_nodes()
#     nedges = net.number_of_edges()
# 
#     cc = x.closeness_centrality(net)
#     cc_ = sorted(cc.items(), key=lambda x: x[1])
#     s1 = set([i[0] for i in cc_[-50:]])
# 
#     bc = x.betweenness_centrality(net)
#     bc_ = sorted(bc.items(), key=lambda x: x[1])
#     s2 = set([i[0] for i in bc_[-50:]])
# 
#     n_both = len(s1 & s2)
# 
#     data.append([nnodes, nedges, n_both, cc_, bc_])
#     print([nnodes, nedges, n_both, cc_, bc_])
# 
# 
# pickle.dump(data,open('../data/nets2.pickle', 'wb'),-1)
data = pickle.load(open('../data/nets2.pickle', 'rb'))

p.clf()
for dp in data:
    # p.plot([dp[0], dp[0]], [dp[1]-10*dp[2], dp[1]+10*dp[2]])
    p.text(dp[0], dp[1], str(dp[2]))
    print(dp[0], dp[1], str(dp[2]))
nn = [i[0] for i in data]
en = [i[1] for i in data]
p.xlim(min(nn)-10, max(nn)+10)
p.ylim(min(en)-10, max(en)+10)
p.savefig('../figs/netHip.png')

def plotInt(data, topn=50):
    p.ion()
    p.clf()
    for dp in data:
        s1 = set([i[0] for i in dp[-2][-topn:]])
        s2 = set([i[0] for i in dp[-1][-topn:]])
        nboth = len(s1 & s2)
        p.text(dp[0], dp[1], str(nboth))
    p.xlim(min(nn)-10, max(nn)+10)
    p.ylim(min(en)-10, max(en)+10)
    p.show()

