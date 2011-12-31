#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

def get_word_from_sogou_txt_dict(fname):
    f = open(fname, 'r')
    for line in f:
        pinyin, string = line.strip().split(' ')
        yield pinyin, string
    f.close()

def showtxt(records):
    for (pystr, utf8str) in records:
        print len(unicode(utf8str, 'utf-8')), utf8str

def main(path):
    generator = get_word_from_sogou_txt_dict(path)
    showtxt(generator)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Please specify the sogou pinyin txt dict file'
        sys.exit(1)
    main(sys.argv[1])
