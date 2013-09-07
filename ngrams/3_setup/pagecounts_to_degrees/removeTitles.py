# -*- coding: utf-8 -*-
import json

def init():
    languages = ['de', 'ru', 'it', 'es', 'fr', 'en']

    for language in languages:
        path = \
        'C:/Users/Elias/Dropbox/__WikiNetworks/Master_Projekt/Analysis/Pagecounts_to_Degree/' +\
        language
        
        with open(path, 'r') as diff:
            differences = json.load(diff)
            
        newdif = {}
        count = 0
        for key, value in differences.iteritems():
            count += 1
            newdif[count] = value
        
        #newdif.append(value for key, value in differences.iteritems())
        print str(len(newdif))
        with open(path + '_stripped.json', 'w') as result:
            json.dump(newdif, result)
                                            
if __name__ == '__main__':
    init()