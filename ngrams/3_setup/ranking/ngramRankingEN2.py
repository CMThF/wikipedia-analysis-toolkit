# -*- coding: utf-8 -*-
import json

def init():
    languages = ['en']
    ngrampath = 'C:/Users/Clemens/My Documents/My Dropbox/WikiNetworks/Master_Projekt/ngrams/'
    
    for language in languages:
    
        print language
        twogrampath = ngrampath + language + '/2gram/total.sorted'
        twogram = []
        average = False
        old_count = 0
        last_rank = 1
        start_position = 0
        end_position = 0
        with open(twogrampath, 'r') as og:
            for ogrank, line in enumerate(og):
                line = line.decode('utf-8').split('\t')
                title = line[0]
                count = int(line[1])
                if old_count == count:
                    if average is False:
                        if ogrank == 0:
                            start_position = 0
                        else:
                            start_position = ogrank - 1
                    twogram.append((title, last_rank, 0))
                    average = True
                else:
                    if average is True:
                        end_position = ogrank - 1
                        average_rank = (start_position + 1.0 + end_position + 1.0) / 2.0
                        for i in range(start_position, end_position + 1):
                            twogram[i] = (twogram[i][0], twogram[i][1], average_rank)
                        average = False
                    twogram.append((title, ogrank + 1, ogrank + 1))  #we count from 1 to x (for difference)
                    last_rank = ogrank + 1
                old_count = count
            if average is True:
                end_position = len(twogram) - 1
                average_rank = (start_position + 1.0 + end_position + 1.0) / 2.0
                for i in range(start_position, end_position + 1):
                    twogram[i] = (twogram[i][0], twogram[i][1], average_rank)
                
        print 'twograms loaded'
            
        with open(ngrampath + language + '/2gram/twogram_ranking.json', 'w') as w:
            json.dump(twogram, w)
            
        print 'twograms dumped'
        
if __name__ == '__main__':
    init()