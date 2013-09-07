# -*- coding: utf-8 -*-
import json

def init():
    languages = ['en']
    degreepath = 'C:/Users/Elias/Dropbox/__WikiNetworks/Master_Projekt/Degrees/results/'
    
    
    for language in languages:
        print language
        
        totaldegpath = degreepath + language + '_deg_titles.sorted'
   
        degrees = []
        average = False
        old_degree = 0
        last_rank = 1
        start_position = 0
        end_position = 0
        with open(totaldegpath, 'r') as deg:
            for degrank, line in enumerate(deg):
                line = line.decode('utf-8').split('\t')
                title = line[0]
                degree = int(line[1])
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
                        for i in range(start_position, end_position + 1):
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
                
        print 'degrees loaded'
        
        with open(degreepath + language + '_ranking.json', 'w') as w:
            json.dump(degrees, w)
            
        print 'degrees dumped'
                       
if __name__ == '__main__':
    init()