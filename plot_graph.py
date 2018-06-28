from igraph import *
import pickle
import random

#open links
with open('./all_links.pkl', 'rb') as f:
    links = pickle.load(f)

#open ranks and create ranks list
ranks = {}
with open('./ranks2.txt', 'rb') as t:
    for line in t:
        splitLine = line.decode().split(':')
        ranks[splitLine[0]] = float(splitLine[1])

#create dictionary of atrticles to numbers in alphabetical order
articles = {}
j = 0
for row in links:
    articles[row['source']] = 0
    articles[row['dest']] = 0

i = 0
for name in sorted(articles.keys()):
    articles[name] = i
    i += 1

n = len(articles)

#read the graph
g = Graph.Read_Pickle("graph.pkl")
#delete n-40 vertices randomly and plot
g.delete_vertices(random.sample(range(0, n), n - 40))
layout = g.layout("kk")
plot(g, layout=layout, bbox=(1080, 1360), margin=100,
     vertex_size=[(100000 * ranks[name])
     if (100000 * ranks[name]) > 10 else 10 for name in g.vs["label"]])
