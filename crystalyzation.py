#!/usr/bin/env python
import json
import re
import pdb

this =json.loads(open("xwordspine.json").read())

def boardtrim(this):
    destroy = 1
    for each in this[-1]:
        if each is ' ':
            pass
        else:
            destroy = 0
    if destroy == 1:
        this.pop(-1)
        boardtrim(this)
    elif destroy == 0:
        print('trimmed')


boardtrim(this)
this = list(zip(*this))
boardtrim(this)
this = list(zip(*this))

for each in this: print(each)

#place 1 horizontal
#wordbones = ""
#for each_square in this[0]:
#    wordbones += each_square.replace(' ','.')
#for each_square in range(len(this[1])):
#    if this[1][each_square] is ' ': 
#        pass
#    else: 
#        print(wordbones[each_square])
        #wordbones[each_square] = this[0][each_square].replace(' ','!')
#print(wordbones)
#mystery_word = re.compile(wordbones)
pdb.set_trace()
#place -1 horizontal

