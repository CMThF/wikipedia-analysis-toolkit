# -*- coding: utf-8 -*-
import json
from math import fabs

def init():
    languages = ['en'] # ['de', 'ru', 'it', 'es', 'fr']
    degreepath = 'C:/Users/Elias/Dropbox/__WikiNetworks/Master_Projekt/Degrees/results/'
    ngrampath = 'C:/Users/Elias/Dropbox/__WikiNetworks/Master_Projekt/ngrams/'
    
    for language in languages:
        print language
        totaldegpath = degreepath + language + '_rankingSmall.json'
        onegrampath = ngrampath + language + '/1gram/onegram_ranking.json'
        twogrampath = ngrampath + language + '/2gram/twogram_ranking'
        resultpath = \
          'C:/Users/Elias/Dropbox/__WikiNetworks/Master_Projekt/Analysis/Degree_to_Ngrams/' +\
          language
        
        with open(totaldegpath, 'r') as deg:
            degrees = json.load(deg)
        print 'degrees loaded'
        
        onegrams = {}
        with open(onegrampath, 'r') as og:
            onegram_list = json.load(og)
        for x in onegram_list:
            onegrams[x[0]] = (x[1], x[2])
        onegram_list = []
        print 'onegrams loaded'
        
        
        searched1 = 0
        searched2 = 0
        found1 = 0
        found2 = 0

        resultdict = {}
        finish = 0
        
        
        for i in range(0,5):
            twograms = {}
            with open(twogrampath + str(i) + '.json', 'r') as tg:
                twogram_list = json.load(tg)
            for x in twogram_list:
                twograms[x[0]] = (x[1], x[2])
            twogram_list = []
            print 'twograms ' + str(i) + ' loaded'
            for count, page in enumerate(degrees):
                if (found1 + found2) >= 10000:
                    break
                title = page[0]
                comp_rank = float(page[1])
                frac_rank = float(page[2])
                grams = title.count('_')
                if grams  == 0:
                    searched1 += 1
                    if onegrams.has_key(title):
                        found1 += 1
                        ng_comp_rank = float(onegrams[title][0])
                        ng_frac_rank = float(onegrams[title][1])
                        dif_comp = fabs(comp_rank - ng_comp_rank)
                        dif_frac = fabs(frac_rank - ng_frac_rank)
                        resultdict[title] = ((dif_comp, dif_frac), (comp_rank, frac_rank), (ng_comp_rank, ng_frac_rank))
                        degrees[count] = 0
                elif grams == 1:
                    searched2 += 1
                    if twograms.has_key(title):
                        found2 += 1
                        ng_comp_rank = float(twograms[title][0])
                        ng_frac_rank = float(twograms[title][1])
                        dif_comp = fabs(comp_rank - ng_comp_rank)
                        dif_frac = fabs(frac_rank - ng_frac_rank)
                        resultdict[title] = ((dif_comp, dif_frac), (comp_rank, frac_rank), (ng_comp_rank, ng_frac_rank))
                        degrees[count] = 0
            degrees = [x for x in degrees if x is not 0]
             
        print 'Dumping result in JSON....'
        
        with open(resultpath, 'w') as result:
            json.dump(resultdict, result)
            
        
        print 'Done!'
        print 'Searched ' + str(finish) + ' pages in Ngrams.'
        print str(found1) + ' of ' + str(searched1) + ' 1grams found.'
        print str(found2) + ' of ' + str(searched2) + ' 2grams found.'
        print 'Total : ' + str(found1 + found2) + ' of ' + str(searched1 + searched2) + ' Ngrams found. Dictionary: ' + str(len(resultdict))
                    
                    
if __name__ == '__main__':
    init()