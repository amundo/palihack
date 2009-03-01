#!/usr/bin/env python
# coding: utf-8

def LCS(S, T):
  # from Wikibook link above
  m = len(S); n = len(T)
  L = [[0] * (n+1) for i in xrange(m+1)]
  lcs = 0
  for i in xrange(m):
    for j in xrange(n):
      if S[i] == T[j]:
        L[i+1][j+1] = L[i][j] + 1
        lcs = max(lcs, L[i+1][j+1])
  return S[:lcs]
 
def extract_stem(formlist):
  stem = LCS(formlist[0], formlist[1])
  for i in range(len(formlist)-1):
    stem = LCS(stem, formlist[i])   
  return stem
    

formlist = "upasaṃkami upasaṃkamiṃsu upasaṃkami upasaṃkamittha upasaṃkamiṃ upasaṃkamiṃhā upasaṃkamimha".split()

print extract_stem(formlist)
