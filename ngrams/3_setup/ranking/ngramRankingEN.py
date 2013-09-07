# -*- coding: utf-8 -*-
import json

def init():
    languages = ['en']
    ngrampath = 'C:/Users/Clemens/My Documents/My Dropbox/WikiNetworks/Master_Projekt/ngrams/'
    
    for language in languages:
    
        print language
        onegrampath = ngrampath + language + '/1gram/total.sorted'
        twogrampath = ngrampath + language + '/2gram/total.sorted'
       
        onegram = []
        average = False
        old_count = 0
        last_rank = 1
        start_position = 0
        end_position = 0
        with open(onegrampath, 'r') as og:
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
                    onegram.append((title, last_rank, 0))
                    average = True
                else:
                    if average is True:
                        end_position = ogrank - 1
                        average_rank = (start_position + 1.0 + end_position + 1.0) / 2.0
                        for i in range(start_position, end_position + 1):
                            onegram[i] = (onegram[i][0], onegram[i][1], average_rank)
                        average = False
                    onegram.append((title, ogrank + 1, ogrank + 1))  #we count from 1 to x (for difference)
                    last_rank = ogrank + 1
                old_count = count
            if average is True:
                end_position = len(onegram) - 1
                average_rank = (start_position + 1.0 + end_position + 1.0) / 2.0
                for i in range(start_position, end_position + 1):
                    onegram[i] = (onegram[i][0], onegram[i][1], average_rank)
                
        print 'onegrams loaded'
        with open(ngrampath + language + '/1gram/onegram_ranking.json', 'w') as w:
            json.dump(onegram, w)
        print 'onegrams dumped'
        onegram = []

                       
if __name__ == '__main__':
    init()