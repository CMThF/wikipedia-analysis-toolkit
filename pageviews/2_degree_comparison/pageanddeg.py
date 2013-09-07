# -*- coding: utf-8 -*-
import sys
import os
import json

def init():
    languages = ['en', 'it', 'fr', 'ru', 'es'] #, 'de']

    p = 'P:/Master_Projekt/201212/filtered'
    d = 'P:/Dropbox/WikiNetworks/Master_Projekt/Degrees/results/'
    e = 'P:/Master_Projekt/201212/sum/'

    dicts = get_all_dicts(d, languages)
    linecount = 0
    successcount = 0
    print 'dictionaries fertig aufgebaut'
    
    directory = os.path.join(p)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith('pagecounts'):
                print file + ' startet'
                with open(file, 'r') as f:
                    for line in f:
                        linecount = linecount + 1
                        splitted = line.split('\t')
                        for lang in languages:
                            if splitted[0] == lang:
                                splitted[1] = splitted[1].replace(' ', '_')
                                if splitted[1] in dicts[lang]:
                                    dicts[lang][splitted[1]] += int(splitted[2])
                                    successcount += 1 #successcount + 1
                        if linecount % 10000 == 0:
                            sys.stdout.write('.')
                            sys.stdout.flush()
                print '\n' + file + ' fertig, successcount = ' + str(successcount)
                                
    print_results(e, languages, dicts)

    print str(successcount) + ' of ' + str(linecount) + ' successfully matched for all languages (except de)'

    
def print_results(e, languages, dicts):
    for lang in languages:
        with open(e+lang+'.json','w') as result:
            json.dump(dicts[lang], result)
    
    
def get_all_dicts(d, languages):
    dicts = {}
    for lang in languages: 
        ld = {}
        linecount = 0
        successcount = 0
        with open(d+lang+'_deg_titles.sorted', 'r') as deg:
            for line in deg:
                ld[line.split('\t')[0]] = 0
        dicts[lang] = ld
    return dicts
        

if __name__ == '__main__':
    init()