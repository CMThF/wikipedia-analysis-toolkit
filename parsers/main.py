# coding: UTF-8

import sys
import page_parser
import externallinks_parser
import pagelinks_parser
import redirects_parser
import finalize

def runAll():
       
    print 'Starting parser for ' +sys.argv[1]+ ' sql files.'
    path = sys.argv[1]
    page_parser.init(arg)
    print 'Pages parsed.'
    pagelinks_parser.init(arg)
    print 'Pagelinks parsed.'
    redirects_parser.init(arg)
    print 'Redirects parsed.'
    externallinks_parser.init(arg)
    print 'Externallinks parsed.'
    finalize.init(arg)
    print 'Dataset complete.'


if __name__ == '__main__':
    runAll()
