#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
import os, sys
from import_sogou_celldict import get_word_from_sogou_cell_dict
from import_sogou_txtdict import get_word_from_sogou_txt_dict
from pymmseg import mmseg

def test(text):
    mmseg.dict_load_defaults()
    algor = mmseg.Algorithm(text)
    for tok in algor:
        print '%s [%d..%d]' % (tok.text, tok.start, tok.end)
    #text = '''今天的天气真好啊，我们一起出去玩一下吧'''
    #algor = mmseg.Algorithm(text)
    #for tok in algor:
    #    print '%s [%d..%d]' % (tok.text, tok.start, tok.end)

def generate_dic_by_cell_dict(path):
    dict_path = '/usr/local/lib/python2.6/site-packages/pymmseg/data/words_new.dic'
    with open(dict_path, 'a+') as fp:
        fp.writelines(['%s %s%s' % (len(word), word.encode('utf-8'), os.linesep) for (req, word) in get_word_from_sogou_cell_dict(path)])

def generate_dic_by_txt_dict(path):
    dict_path = '/usr/local/lib/python2.6/site-packages/pymmseg/data/words_new.dic'
    with open(dict_path, 'a+') as fp:
        fp.writelines(['%s %s%s' % (len(unicode(word, 'utf-8')), word, os.linesep) for (req, word) in get_word_from_sogou_txt_dict(path)])

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print 'Please input datasource path'
        sys.exit()
    #generate_dic_by_cell_dict(sys.argv[1])
    #generate_dic_by_txt_dict(sys.argv[1])
    test(sys.argv[1])
    #for cell_file in os.listdir(sys.argv[1]):
    #    print cell_file
    #    generate_dic_by_cell_dict('%s/%s' % (sys.argv[1], cell_file))
