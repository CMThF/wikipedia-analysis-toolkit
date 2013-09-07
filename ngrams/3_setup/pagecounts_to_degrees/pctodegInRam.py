# -*- coding: utf-8 -*-
import json
from math import fabs

def init():
    languages = ['it']#['de', 'ru', 'it', 'es', 'fr', 'en']
    degreepath = 'C:/Users/Elias/Dropbox/__WikiNetworks/Master_Projekt/Degrees/results/'
    for language in languages:
        print language
        pagecountpath = \
          'C:/Users/Elias/Dropbox/__WikiNetworks/Master_Projekt/Acesslogs/results/top1000/' +\
          language + '_pagecounts_with_rankings.json'
        totaldegpath = degreepath + language + '_ranking.json'
        resultpath = \
          'C:/Users/Elias/Dropbox/__WikiNetworks/Master_Projekt/Analysis/Pagecounts_to_Degree/' +\
          language
        
        with open(pagecountpath, 'r') as pc:
            pagecounts = json.load(pc)
        
        print 'pagecounts loaded'
        
        
        #rausspeichern von dict mit gefunden onegrams und count, gleiches für pagecounts -->plottten
        #bei dict schwer startswith zu verwenden, vorfiltern und alle klammern begriffe rausschmeißen?
        degrees = {}
        with open(totaldegpath, 'r') as deg:
            degree_list = json.load(deg)
        for x in degree_list:
            degrees[x[0]] = (x[1], x[2])
        degree_list = []   
        print 'degrees loaded'

        
        #trennen in 1gram, 2gram, bzw mitspeichern oder nur über titel.count('_') verfügbar?
        resultdict = {}
        found = 0
        
        for count, page in enumerate(pagecounts):
            if count + 1 > 10000:
                break
            title = page[0]
            comp_rank = float(page[1])
            frac_rank = float(page[2])
            if degrees.has_key(title):
                found += 1
                deg_comp_rank = float(degrees[title][0])
                deg_frac_rank = float(degrees[title][1])
                dif_comp = fabs(comp_rank - deg_comp_rank)
                dif_frac = fabs(frac_rank - deg_frac_rank)
                resultdict[title] = ((dif_comp, dif_frac), (comp_rank, frac_rank), (deg_comp_rank, deg_frac_rank))  
            else:
                print 'ups'
         
        print 'Dumping result in JSON....'
        
        with open(resultpath, 'w') as result:
            json.dump(resultdict, result)

        print 'Done!'
        
        print 'Total : ' + str(found) + '/10000 Degrees found. Dictionary: ' + str(len(resultdict))
                        
                        
if __name__ == '__main__':
    init()