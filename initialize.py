import numpy as np
import pickle

#load the links from load_corpus.py
with open('./all_links.pkl', 'rb') as f:
    links = pickle.load(f)

#dictionary of articles(nodes) 
articles = {}
for row in links:
    articles[row['source']] = []
    articles[row['dest']] = []

#each article is mapped to a list of its outlinks
for row in links:
    articles[row['source']].append(row['dest'])

n = len(articles)
M = np.zeros((n,n))

index = {}
t = 0

#map every article to a number in alphabetical order
for i in sorted(articles.keys()):
    index[i] = t
    t += 1

assert(t==n)

#create web matrix M
for i,j in enumerate(sorted(articles.keys())):
    k = len(articles[j])
    if k!=0:
        for l in articles[j]:
            M[index[l]][i] = 1/k
#save M and articles
with open('./matrixM.pkl','wb') as f:
    pickle.dump(M,f)
with open('./articles.pkl','wb') as f:
    pickle.dump(articles,f)
