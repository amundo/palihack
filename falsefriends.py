from glob import glob
import lev
import sys
import os
from difflib import get_close_matches

UDHR = '/home/pat/whatlang/udhr/'

def udhr(code): 
 text = open(UDHR + os.sep + 'udhr_' + code + '.txt').read().decode('utf-8')
 #print text[:100].encode('utf-8')
 return text

def tokenize(text):  
 fixed = [] 
 for c in text:
  if c in '?.!;,"\'': fixed.append(' ') 
  else: fixed.append(c)
 return ''.join(fixed).lower().split()

class Text:
 def __init__(self, code):
  self.code = code
  self.text = udhr(code)
  self.words = tokenize(self.text)
  self.vocab = set(self.words)


if __name__ == "__main__":
 spanish = Text('spa')
 english = Text('eng')

 matches = []

 for s in spanish.vocab: 
  #print s.encode('utf-8')
  for e in english.vocab:
   matches.append((lev.distance(e,s), e,s))

 for x,y,z in matches:
  if len(y) > 6 and x > 2 and x < 4: print x,y,z
