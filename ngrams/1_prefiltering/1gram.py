
import sys
import os
import gzip

def init():
    p = 'D:/MasterProjekt/ngrams/de/2gram'
    taglist = ['_NOUN', '_VERB', '_ADJ', '_ADP', '_ADV', '_CONJ', '_DET', '_PRON', '_NUM', '_PRT', '_.', '_X']
    sum = 0
    directory = os.path.join(p)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith('googlebooks-ger-all-2gram'):
                x= open('filtered_'+file.rsplit('.', 1)[0]+'.dat', 'w')
                f= gzip.open(file, 'r')
                for line in f:
                    parted = line.split('\t')
                    if parted[1] == '2009':
                        tsplit = parted[0].split(' ')
                        if ignoreMe(tsplit):
                            continue
                        title = stripMe(tsplit, taglist)
                        sum += int(parted[2])
                        x.write(title + '\t' + parted[2] + '\n')
                f.close()
                x.close()
                print file + ' done'
    print 'Total sum: ' + str(sum) + '.'

def ignoreMe(ngram):
    for x in ngram:
        if x.startswith('_') and x.endswith('_'):
            return True
    return False
    
def stripMe(ngram, taglist):
    stripped = ''
    for x in ngram:
        for z in taglist:
            if x.endswith(z):
                x = x.rsplit('_',1)[0]
                break
        stripped += x + '_'
    return stripped.rsplit('_',1)[0]
            
    
if __name__ == '__main__':
    init()