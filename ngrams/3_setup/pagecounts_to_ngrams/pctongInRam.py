# -*- coding: utf-8 -*-
import json
from math import fabs

def init():
    langs = ['en'] #['de', 'ru', 'it', 'es', 'fr'] # en fehlt
    for language in langs:
        print language
        
        pagecountpath = \
          'C:/Users/Elias/Dropbox/__WikiNetworks/Master_Projekt/Acesslogs/results/top1000/' +\
          language + '_pagecounts_with_rankings.json'
        ngrampath = 'C:/Users/Elias/Dropbox/__WikiNetworks/Master_Projekt/ngrams/'
        onegrampath = ngrampath + language + '/1gram/onegram_ranking.json'
        twogrampath = ngrampath + language + '/2gram/twogram_ranking'
        resultpath = \
          'C:/Users/Elias/Dropbox/__WikiNetworks/Master_Projekt/Analysis/Pagecounts_to_Ngrams/' +\
          language
        
        with open(pagecountpath, 'r') as pc:
            pagecounts = json.load(pc)
        
        print 'pagecounts loaded'
        #pagecounts = pagecounts[0:40000]
        
        onegrams = {}
        onegrams_list = []
        with open(onegrampath, 'r') as onegram:
            onegrams_list = json.load(onegram)
        for x in onegrams_list:
            onegrams[x[0]] = (x[1], x[2])
        
        print 'onegrams loaded'
        onegrams_list = []
        
        
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
            for idx, page in enumerate(pagecounts):
                if (found1 + found2) >= 10000:
                    break

                title = page[0]
                competition_pcrank = page[1]
                fractional_pcrank = page[2]
                grams = title.count('_')
                if grams  == 0:
                    searched1 += 1
                    if onegrams.has_key(title):
                        found1 += 1
                        competition_ngrank = onegrams[title][0]
                        fractional_ngrank = onegrams[title][1]
                        competition_dif = fabs(competition_pcrank - competition_ngrank)
                        fractional_dif = fabs(fractional_pcrank - fractional_ngrank)
                        resultdict[title] = ((competition_dif, fractional_dif), 
                                            (competition_pcrank, fractional_pcrank), 
                                            (competition_ngrank, fractional_ngrank))
                        pagecounts[idx] = 0
                      
                elif grams == 1:
                    searched2 += 1
                    if twograms.has_key(title):
                        found2 += 1
                        competition_ngrank = twograms[title][0]
                        fractional_ngrank = twograms[title][1]
                        competition_dif = fabs(competition_pcrank - competition_ngrank)
                        fractional_dif = fabs(fractional_pcrank - fractional_ngrank)
                        resultdict[title] = ((competition_dif, fractional_dif), 
                                            (competition_pcrank, fractional_pcrank), 
                                            (competition_ngrank, fractional_ngrank))
                        pagecounts[idx] = 0
            pagecounts = [x for x in pagecounts if x is not 0]
         
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