from urllib.parse import unquote
import csv
import pickle

#read the links files
with open('./corpus/links.tsv') as links:
    l = []
    #read the tsv file and delimit on tabs
    reader = csv.DictReader(links,delimiter = '\t')
    for row in reader:
        l.append(row)
    #delete the first ten lines of comments in the tsv file
    l = l[10:]
    for row in l:
    	#unquote to parse the url formating of the links
        row['source'] = unquote(unquote(row.pop('# The list of all links between articles.')))
        row['dest'] = unquote(unquote(row.pop(None)[0]))
    #save l
    with open('./all_links.pkl','wb') as f:
        pickle.dump(l,f)
