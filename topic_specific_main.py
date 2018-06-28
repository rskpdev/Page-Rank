from power_iteration import PageRank
import pickle

with open('./topic_wise.pkl', 'rb') as f:
    t = pickle.load(f)
with open('./matrixM.pkl', 'rb') as f:
    M = pickle.load(f)
with open('./articles.pkl', 'rb') as f:
    articles = pickle.load(f)

#create a topic set
topic_set = set()
for i in t:
    topic_set.add(i['topic'])

#create a dictionary of topics
article_topic = {key : [] for key in topic_set}

#add articles to the topics
for i in t:
    article_topic[i['topic']].append(i['article'])

topic_set = sorted(list(topic_set))
print("\nSelect from the following topics: \n")
for i,topic in enumerate(topic_set):
    print(i,topic)
choice = int(input("Enter index to select:"))
#create a teleport set based on the user choice
teleport_set = article_topic[topic_set[choice]]

print("pages belonging to this category are:\n")
for i in teleport_set:
    print(i)

#run the Page Rank algorithm
rank, iterations = PageRank(M,articles,teleport_set,topic_specific = True)
with open('ranks2.txt','w') as f:
    for i in rank:
        f.write(i[0] + ':' + str(i[1]) + '\n')
