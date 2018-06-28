import pickle
import numpy as np
import operator

def PageRank(M, articles, teleport_set = None, topic_specific = False, epsilon = 1.0e-8, d = 0.85):
    """power iteration for PageRank"""
    index = {}
    t = 0

    #map every article to a number in alphabetical order
    for i in sorted(articles.keys()):
        index[i] = t
        t += 1
    iterations = 0
    error = 2**10
    n = M.shape[0]
    v0 = np.zeros((n,1))
    for i in range(n):
        v0[i][0] = 1/n
    new_v = v0
    one = np.ones((n,1))

    #remove from one if not in teleport set
    if topic_specific == True:
        for i,j in index.items():
            if i not in teleport_set:
                one[j][0] = 0

    #loop until error is less than the specified value
    while error > epsilon:
        old_v = new_v
        if topic_specific == True:
            k = len(teleport_set)
            new_v = d*np.matmul(M,old_v) + ((1-d)/k)*one
        else:
            new_v = d*np.matmul(M,old_v) + ((1-d)/n)*one
        error = np.sum(np.absolute(new_v-old_v),0)
        iterations += 1
    rank = []
    mapping = {}
    for i in range(n):
        for a in index.keys():
            if i == index[a]:
                mapping[a] = new_v[i][0]
    for w in sorted(mapping, key=mapping.get, reverse=True):
        rank.append([w,mapping[w]])
    return rank,iterations

with open('./matrixM.pkl', 'rb') as f:
    M = pickle.load(f)
with open('./articles.pkl', 'rb') as f:
    articles = pickle.load(f)

rank, iterations = PageRank(M,articles)

with open('ranks1.txt','w') as f:
    for i in rank:
        f.write(i[0] + ':' + str(i[1]) + '\n')
