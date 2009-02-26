#!/usr/bin/env python
# coding: utf-8

rules = u"""ā	aa
ī	ii
ū	uu
ṃ	.m
ṇ	.n
ñ	~n
ṭ	.t
ḍ	.d
ṅ	"n
ḷ	.l""".strip().splitlines()

scheme = []

def sortbykeylen(pairs):
  return sorted([(v,k) for k,v in dict(pairs).items()], key=lambda x: len(x[0]))

def flippairs(pairs):
  return [(b,a) for a,b in pairs]

for rule in rules:
  print rule
  unicode, velthuis = rule.split()
  scheme.append((velthuis, unicode))

def dumpscheme(scheme):
  for a,b in scheme: print a,b

unicode2velthuis = sortbykeylen(scheme)
velthuis2unicode = flippairs(unicode2velthuis)

"""
dumpscheme( unicode2velthuis)
print
dumpscheme( velthuis2unicode)
"""

def transliterate(scheme, text):
  transliterated = []
  for before, after in scheme:
    text = text.replace(before,after)
  return text
  

if __name__ == "__main__":
  import sys
  source  = sys.argv[1].decode('utf-8')
  print transliterate(velthuis2unicode, source)

