#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '25.txt'
inp = open(filename)

import networkx as nx
import random

nodes = []
G = nx.Graph()
for line in inp:
    v, *w = line.replace(':', ' ').split()
    nodes.append(v)
    G.add_edges_from((v, w, {'capacity': 1}) for w in w)

while True:
    v, w = random.sample(nodes, 2) # lol
    cut, part = nx.minimum_cut(G, v, w)
    if cut == 3:
        print(math.prod(len(p) for p in part))
        break
