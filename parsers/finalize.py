# coding: UTF-8
import hashlib
import sys
import json
from collections import defaultdict

def init(arg):

    """Pages"""
    pages = defaultdict(set)
    page_state = 0
    page_id = 0
    page_list = 0
    with open('../results/pages.txt', 'r', 1024) as f:
        for line in f:
            line = line.decode('utf-8', 'replace')
            if page_state == 0:
                page_id = line.strip()
                page_state = 1
                continue
            if page_state == 1:
                dlt = ']'
                line = [tup+dlt for tup in line.strip().split(dlt) if tup != '']
                for k in line:
                    #pages[page_id].add(tuple(json.loads(k)))
                    info = json.loads(k)
                    pages[info[1]].add((page_id, info[0]))
                page_state = 0
                continue

    print "Pages have been imported."
    
    """Redirects"""
    redirects = {}
    rdr_state = 0
    rdr_id = 0
    rdr_list = 0
    with open('../results/redirect.txt', 'r', 1024) as f:
        for line in f:
            line = line.decode('utf-8', 'replace')
            if rdr_state == 0:
                rdr_id = line.strip()
                rdr_state = 1
                continue
            if rdr_state == 1:
                dlt = ']'
                line = [tup+dlt for tup in line.strip().split(dlt) if tup != '']
                for k in line:
                    lookup = tuple(json.loads(k))
                    if lookup[0] is not '0':
                        redirects[rdr_id] = 'ignore'
                    new_id = getId(pages, lookup[0], lookup[1])
                    if new_id == 'notfound':
                        rdr_state = 0
                        continue
                    redirects[rdr_id] = new_id
                rdr_state = 0
                continue

    print "Redirects have been imported."
    
    """Pagelinks"""
    link_state = 0
    link_id = 0
    link_list = 0
    with open('../results/pagelinks.txt', 'r', 1024) as f:
        with open('../results/'+ arg +'.txt', 'w') as pl:
            for line in f:
                line = line.decode('utf-8', 'replace')
                if link_state == 0:
                    link_id = line.strip()
                    link_state = 1
                    continue
                if link_state == 1:
                    dlt = ']'
                    line = [tup+dlt for tup in line.strip().split(dlt) if tup != '']
                    for k in line:
                        lookup = tuple(json.loads(k))
                        new_id = getId(pages, lookup[0], lookup[1])
                        if new_id == 'notfound':
                            link_state = 0
                            continue
                        #tmp = link_id + '\t' + lookup[0] + 's' + str(new_id) + '\n'
                        rdr = []
                        if new_id in redirects:
                            rdr = redirects[new_id]
                            if rdr is not 'ignore':
                                new_id = rdr
                                tmp = link_id + '\t' + new_id + '\n'
                                pl.write(tmp.encode('utf-8'))
                        else:
                            tmp = link_id + '\t' + new_id + '\n'
                            pl.write(tmp.encode('utf-8'))
                        
                    link_state = 0
                    continue

    print "Pagelinks updated."
                
    """External Links"""
    externals = {}
    with open('../results/externallinks.txt', 'r', 1024) as e:
        externals = json.load(e)
    with open('../results/final_links.txt', 'a') as fl:
        for k in externals.iteritems():
            linkhash = hashlib.md5(k[1].encode('utf-8')).hexdigest()
            tmp = k[0] + '\t' + linkhash + '\n'
            fl.write(tmp.encode('utf-8'))

    print "Externallinks added."

    
"""
def getKey(dict, namespace, value):
    #id = [k for k,v in dict.iteritems() if v  == value]#[0]
    new_id = 'broken'
    for k in dict.iteritems():
        for i in k[1]:
            #if i[1] == value:
            #    new_id = k[0]
            if (i[0] == namespace) and (i[1] == value):
                new_id = k[0]
                break
    return new_id
"""
def getId(pages, namespace, value):
    new_id = 'notfound'
    tmp = pages[value]
    if not tmp:
        return new_id
    for k in tmp:
        if int(k[1]) == int(namespace):
            if int(k[1]) is not 0:
                new_id = 'ignore'
                break
            new_id = k[0]
            break
    return new_id
    


if __name__ == '__main__':
    init()
