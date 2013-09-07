# -*- coding: utf-8 -*-
import json   

def init():
    langs = ['en'] # en fehlt
    for language in langs:
        path = 'C:/Users/Clemens/Documents/My Dropbox/WikiNetworks/Master_Projekt/Acesslogs/results/top1000/'
        pagecountpath = path + language + '_top1000.json'
        gogoranking(pagecountpath, language, path)
    
def gogoranking(pagecountpath, language, path):
    #elias deg code verwurstet
    degrees = []
    average = False
    old_degree = 0
    last_rank = 1
    start_position = 0
    end_position = 0
    with open(pagecountpath, 'r') as pc:
        pagecounts = json.load(pc) #list
    print 'pagecounts loaded'

    for degrank, line in enumerate(pagecounts):
        if degrank >= 100000:
            break
        title = line[0]
        degree = line[1]
        if old_degree == degree:
            if average is False:
                if degrank == 0:
                    start_position = 0
                else:
                    start_position = degrank - 1
            degrees.append((title, last_rank, 0))
            average = True
        else:
            if average is True:
                end_position = degrank - 1
                average_rank = (start_position + 1.0 + end_position + 1.0) / 2.0
                for i in range(start_position, end_position+1):
                    degrees[i] = (degrees[i][0], degrees[i][1], average_rank)
                average = False
            degrees.append((title, degrank + 1, degrank + 1))  #we count from 1 to x (for difference)
            last_rank = degrank + 1
        old_degree = degree
    if average is True:
        end_position = len(degrees) - 1
        average_rank = (start_position + 1.0 + end_position + 1.0) / 2.0
        for i in range(start_position, end_position + 1):
            degrees[i] = (degrees[i][0], degrees[i][1], average_rank)
        average = False
    print 'pagecounts loaded'
    
    with open(path + language + '_pagecounts_with_rankings.json', 'w') as w:
        json.dump(degrees, w)
        
    print language + ' pagecounts dumped'
                       
if __name__ == '__main__':
    init()