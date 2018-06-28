from urllib.parse import unquote
import csv
import pickle

#load catagories from the tsv file
with open('./corpus/categories.tsv') as fields:
    l = []
    reader = csv.DictReader(fields,delimiter = '\t')
    for row in reader:
        l.append(row)
    l = l[11:]
    for row in l:
        row['article'] = unquote(unquote(row.pop('# Hierarchical categories of all articles.')))
        row['topic'] = unquote(unquote(row.pop(None)[0]))
    with open('./topic_wise.pkl','wb') as f:
        pickle.dump(l,f)
