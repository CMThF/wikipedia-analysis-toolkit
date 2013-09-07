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
        dump = False
        dump_count = 0
        dump_lines = 24164997 #120824983 lines laut vim / 5 = 24164996,6
        dump_already_processed = 0
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
                            start_position = ogrank - 1 - dump_already_processed
                    twogram.append((title, last_rank, 0))
                    average = True
                else:
                    if average is True:
                        end_position = ogrank - 1 - dump_already_processed
                        average_rank = (start_position + 1.0 + end_position + 1.0) / 2.0
                        try:
                            for i in range(start_position, end_position + 1):
                                twogram[i] = (twogram[i][0], twogram[i][1], average_rank)
                        except:
                            print 'ERROR with start = ' + str(start_position) + ' and end = ' + str(end_position)
                            print 'length twogram: ' + str(len(twogram))
                            print 'ogrank ' + str(ogrank)
                            print 'dump processed ' + str(dump_already_processed)
                        average = False
                        if dump is True:
                            with open(ngrampath + language + '/2gram/twogram_ranking'+str(dump_count)+'.json', 'w') as d:
                                json.dump(twogram, d)
                                print 'I just dumped a load... ' + str(dump_count) + ' to be precise'
                                dump_count += 1
                                dump_already_processed = (ogrank)#-1)
                                twogram = []
                                dump = False
                    twogram.append((title, ogrank + 1, ogrank + 1))  #we count from 1 to x (for difference)
                    last_rank = ogrank + 1    
                old_count = count
                """ alle dump_lines und nicht in der ersten zeile dumpen wir - aber nur
                    wenn wir nicht in einem average zweig sind. sind wir das, merken wir
                    es uns in dump, und dumpen erst, wenn wir average auf false setzen.
                """
                if ogrank % dump_lines == 0 and ogrank != 0:
                    if average is False:
                        with open(ngrampath + language + '/2gram/twogram_ranking'+str(dump_count)+'.json', 'w') as d:
                            json.dump(twogram, d)
                            print 'I just dumped a load... ' + str(dump_count) + ' to be precise'
                            dump_count += 1
                            dump_already_processed = ogrank
                            twogram = []
                            dump = False
                    else:
                        dump = True
                        
            if average is True:
                end_position = len(twogram) - 1
                average_rank = (start_position + 1.0 + end_position + 1.0) / 2.0
                for i in range(start_position, end_position + 1):
                    twogram[i] = (twogram[i][0], twogram[i][1], average_rank)
                
        print 'twograms loaded'
            
        with open(ngrampath + language + '/2gram/twogram_ranking'+str(dump_count)+'.json', 'w') as w:
            json.dump(twogram, w)
            
        print 'twograms dumped'
        
if __name__ == '__main__':
    init()