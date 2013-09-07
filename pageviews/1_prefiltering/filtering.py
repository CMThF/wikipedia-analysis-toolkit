# -*- coding: utf-8 -*-
import sys
import os
import urllib2
import gzip

def init():
    p = 'O:/Downloads/pagecounts/201202'
    destination = 'P:/Master_Projekt/201202/filtered/'
    directory = os.path.join(p)
    signs_of_death = {'%0A', '%0a', '%1A', '%1a', '%0D', '%0d', '%09'}
    encodings = {'en': 'ISO-8859-2', 'de': 'ISO-8859-2', 'es': 'ISO-8859-2', 
                 'it': 'ISO-8859-2', 'fr': 'ISO-8859-2', 'ru': 'windows-1251'}
    decodeexceptions = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith('pagecounts'):
                f= gzip.open(file, 'r')
                x= open(destination+file.rsplit('.')[0] + '.filtered', 'w')
                for line in f:
                    if (line.startswith('en') or line.startswith('de') or \
                    line.startswith('fr') or line.startswith('es') or \
                    line.startswith('ru') or line.startswith('it')) and \
                    (line.startswith(' ', 2) or line.startswith('.mw', 2, 5)):
                        line = line.rsplit(' ', 1)[0]
                        line = line.split(' ')
                        if len(line) < 2:
                            continue
                        lang = line[0].strip()
                        title = line[1]
                        for i in signs_of_death:
                            title = title.replace(i, '')
                        try:
                            title = urllib2.unquote(title).decode(encodings[lang[:2]])
                        except:
                            try: 
                                title = urllib2.unquote(title).decode('utf-8')
                            except:
                                decodeexceptions = decodeexceptions + 1
                                print file + ', overall Exceptions: ' + str(decodeexceptions)
                        count = line[2].strip()
                        try: 
                            x.write((lang.encode('utf-8') + '\t' + 
                            title.strip().encode('utf-8') + '\t' + 
                            count.encode('utf-8') + '\n'))
                        except:
                            decodeexceptions = decodeexceptions + 1
                            if decodeexceptions % 100 == 0:
                                print file + ', overall Exceptions: ' + str(decodeexceptions)
                f.close()
                x.close()
    print '\ndone, overall Exceptions: ' + str(decodeexceptions)
    
    
    
if __name__ == '__main__':
    init()