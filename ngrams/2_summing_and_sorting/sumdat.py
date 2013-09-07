# -*- coding: utf-8 -*-
import sys
import os
import json
import operator

def init():

    p = 'C:/Users/Elias/Dropbox/__WikiNetworks/Master_Projekt/ngrams/'
    #output_top1000 = 'D:/Dropbox/__WikiNetworks/Master_Projekt/ngrams/top1000/'
    #output_json = 'D:/Dropbox/__WikiNetworks/Master_Projekt/ngrams/sorted/'
    language = 'it'
    xgram = '1gram'
    dict = {}
    #list = []
    
    directory = os.path.join(p + language + '/' + xgram)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.dat'):
                print 'reading file ' + file
                with open(file, 'r') as f:
                    for line in f:
                        line = line.decode('utf-8', 'replace')
                        values = line.split('\t')
                        if values[0] in dict:
                            dict[values[0]] += int(values[1])
                        else:
                            dict[values[0]] = int(values[1])
                
    print 'dict built.'
    
    with open(p + language + '/' + xgram + '/total.dat', 'w') as w:
        for title, count in dict.iteritems():
            w.write((title + '\t' + str(count) + '\n').encode('utf-8'))
        

    print 'DONE.'
    
if __name__ == '__main__':
    init()