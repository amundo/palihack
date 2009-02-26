#!/usr/bin/env python 
# coding: utf-8
from glob import glob
from string import punctuation
from operator import itemgetter
from collections import defaultdict

"""
terms = open('paliverbs.txt').read().decode('utf-8').splitlines()
lex = {}
for line in terms:
 source, term = line.split('\t')
 lex[term] = source
"""

def uread(f):
 return open(f).read().decode('utf-8')

def depunctuate(text):
 res = []
 for c in text:
  if c in punctuation: res.append(u' ')
  else: res.append(c)
 return ''.join(res)

mn = glob('./Majjhima/*')

corpus = u''

for m in mn: corpus += depunctuate(uread(m))

words = corpus.split()

def freq(seq):
 fq = defaultdict(int)
 for e in seq: fq[e] += 1 
 return fq 

palifq = freq(words)

def nohapax(d):
 fixed = {}
 for e in d:
  if d[e] != 1: fixed[e] = d[e]
 return fixed

palifq = nohapax(palifq)

def byvalue(d):
 return sorted(d.iteritems(), key=lambda x: x[1])

if __name__ == "__main__":
 import sys
 from velthuis import transliterate, velthuis2unicode
 stem = sys.argv[1]
 stem = transliterate(velthuis2unicode, stem)
 print stem.upper().encode('utf-8')
 print
 counts = []
 for p, fq in palifq.items():
   if p.startswith(stem): counts.append((fq, p))
 for fq, p in sorted(counts): print fq,p
