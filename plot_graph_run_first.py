from igraph import *
import pickle

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
#create a graph of n vertices
n = len(articles)
g = Graph(directed=True)
g.add_vertices(n)

#create edges
j = 0
for row in links:
    sys.stdout.write("progress: %d%%  \r" % ((j / 119882) * 100))
    sys.stdout.flush()
    g.add_edges([(articles[row['source']], articles[row['dest']])])
    j += 1

g.vs["label"] = sorted(articles.keys())

#save the graph
g.write_pickle("graph.pkl")
