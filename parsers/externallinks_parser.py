# coding: UTF-8
from collections import defaultdict
import json

def init(arg):
    f = open('../sql/'+arg+'-externallinks.sql', 'r', 1024)
    #count = 0
    #dooku = 40
    #final = defaultdict(set)
    final = {}
    """for line in f:
        line = line.decode('utf-8')
        count += 1
        if count >= dooku:
            parse(line, final)"""
    start = 0
    for line in f:
        line = line.decode('utf-8', 'replace')
        if not start:
            start = findStart(line)
        if start:
            parse(line, final)

    with open('../results/externallinks.txt', 'w') as o: 
        """for k, v in final.items():
            for i in v:
                tmp = k + " " + i + '\n'
                o.write(tmp.encode('utf-8'))"""
        json.dump(final, o)

def findStart(line):
    state = 0
    for c in line:
        if state == 0:
            if c == 'I':
                state = 1
        elif state == 1:
            if c == 'N':
                state = 2
            else:
                state = 0
        elif state == 2:
            if c == 'S':
                state = 3
            else:
                state = 0
        elif state == 3:
            if c == 'E':
                state = 4
            else:
                state = 0
        elif state == 4:
            if c == 'R':
                state = 5
            else:
                state = 0
        elif state == 5:
            if c == 'T':
                return 1
            else:
                state = 0
    return  0
        

def parse(line, externals):
    state = 0
    current_id = ''
    current_title = ''
    for c in line:
        if state == 0:
            if c == '(':
                state = 1

        elif state == 1:
            if c == ',':
                state = 3
                continue
            current_id = current_id + c

        elif state == 3:
            if c == '\'':
                state = 31
            elif c == ',':
                state = 4

        elif state == 31:
            if c == '\\':
                state = 32
                continue
            elif c == '\'':
                state = 3
                #dict[current_id].add(current_title)
                externals[current_id] = current_title
                current_id = ''
                current_title = ''
                continue
            current_title = current_title + c
            
        elif state == 32:
            current_title = current_title + c
            state = 31
            
        elif state == 4:
            if c == ')':
                state = 0
            elif c == '\'':
                state = 41
                
        elif state == 41:
            if c == '\\':
                state = 42
            elif c == '\'':
                state = 4

        elif state == 42:
            state = 41

if __name__ == '__main__':
    init()
