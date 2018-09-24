#!/usr/bin/env python

import os 
import random
import sys

def find(needle,haystack):
  if needle == haystack: return []
  # Strings are iterable, too
  if isinstance(haystack,str) and len(haystack)<=1: return None
  try:
    for i,e in enumerate(haystack):
      r = find(needle,e)
      if r is not None: 
        r.insert(0,i)
        return r
  except TypeError:
    pass
  return None    
