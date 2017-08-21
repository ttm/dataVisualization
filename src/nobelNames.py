# from SPARQLWrapper import SPARQLWrapper
import SPARQLWrapper
queryString = """
PREFIX nobel: <http://data.nobelprize.org/terms/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT DISTINCT ?label ?gender ?category
     WHERE {
     ?laur rdf:type nobel:Laureate .
     ?laur rdfs:label ?label .
     ?laur foaf:gender ?gender .
     ?laur nobel:laureateAward ?award .
     ?award nobel:category ?category .
}
"""
sparql = SPARQLWrapper.SPARQLWrapper("http://data.nobelprize.org/sparql",returnFormat=SPARQLWrapper.JSON)
sparql.setQuery(queryString)
ret = sparql.query()

vals = ret.convert()

names = []
cat_names = {}
gen_names = {}
for val in vals['results']['bindings']:
    name = val['label']['value']
    gen = val['gender']['value']
    cat = val['category']['value'].split("/")[-1]
    names.append(name)
    if gen not in gen_names:
        gen_names[gen] = []
    if cat not in cat_names:
        cat_names[cat] = []
    gen_names[gen].append(name)
    cat_names[cat].append(name)

# import pickle
# pickle.dump([names, cat_names, gen_names],open('../data/nobelNames.pickle', 'wb'),-1)
# names, cat_names, gen_names = pickle.load(open('../data/nobelNames.pickle', 'rb'))

names = [i.lower() for i in names]
l = [i[0] for i in names]

l2 = []
for n in names:
    nn = n.split("(")[0].strip().split(" ")
    if len(nn) < 0:
        print(n)
    else:
        l2.append(nn[-1][0])

keys = list(set(l+l2))
keys.sort()

# vals = [0]*len(keys)

# from collections import Counter
h = [keys.index(i) for i in l]
# h_ = Counter(h)
# 
h2 = [keys.index(i) for i in l2]
# h2_ = Counter(h2)

h__ = [h.count(i) for i in range(len(keys))]
h2__ = [h2.count(i) for i in range(len(keys))]

import pylab as p
p.clf()
p.bar(range(len(keys)), h__, tick_label=keys)
p.savefig("../figs/nobelFirst.png")

p.clf()
p.bar(range(len(keys)), h2__, tick_label=keys)
p.savefig("../figs/nobelLast.png")

