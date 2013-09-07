# -*- coding: utf-8 -*-
import sys
import os
import json
import operator

def init():
    p = 'D:/MasterProjekt/pagecounts/sortsum/sum/'
    output_top1000 = 'D:/MasterProjekt/pagecounts/sortsum/top1000/'
    output_json = 'D:/MasterProjekt/pagecounts/sortsum/sorted/'
    languages = ['de', 'en', 'es', 'fr', 'it', 'ru']
    dicts = {}
    for l in languages:
        dicts[l] = {}
        
    print 'loading/adding up dictionaries...'
    
    directory = os.path.join(p)
    for root, dirs, files in os.walk(directory):
        for file in files:
            tmp = json.load(open(file, 'r'))
            if file.startswith('de'):
                dicts['de'] = dict(dicts['de'].items() + tmp.items())
            elif file.startswith('en'):
                dicts['en'] = dict(dicts['en'].items() + tmp.items())
            elif file.startswith('es'):
                dicts['es'] = dict(dicts['es'].items() + tmp.items())
            elif file.startswith('fr'):
                dicts['fr'] = dict(dicts['fr'].items() + tmp.items())
            elif file.startswith('it'):
                dicts['it'] = dict(dicts['it'].items() + tmp.items())
            elif file.startswith('ru'):
                dicts['ru'] = dict(dicts['ru'].items() + tmp.items())
                
    print 'summation done.'
    print 'sorting...'
    
    #sorted_dicts = {}
    for l in languages:
        sorted_list = {sorted(dicts[l].iteritems(), key=operator.itemgetter(1), reverse=True)}
        with open(output_top1000 + l + '_top1000.json', 'w') as x:
            json.dump(sorted_list, x)
        sorted_l_dict = {}
        for idx, item_tuple in enumerate(sorted_list):
            sorted_l_dict[item_tuple[0]] = item_tuple[1], idx
        #sorted_dicts[l] = sorted_l_dict
        
        with open(output_json + l + '_result.json', 'w') as x:
            json.dump(sorted_l_dict, x)
            
    print 'DONE!'
            
           
    
if __name__ == '__main__':
    init()