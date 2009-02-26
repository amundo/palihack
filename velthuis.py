#!/usr/bin/env python
# coding: utf-8
rules = u"""ā	aa
ī	ii
ū	uu
ṁ	.m
ṇ	.n
ñ	~n
ṭ	.t
ḍ	.d
ṅ	"n
ḷ	.l""".strip().splitlines()

unicode2velthuis = {}
velthuis2unicode = {}

for rule in rules:
  print rule
  unicode, velthuis = rule.split()
  unicode2velthuis[unicode] = velthuis
  velthuis2unicode[velthuis] = unicode

print unicode2velthuis
print velthuis2unicode

def transliterate(scheme, text):
 transliterated = []
