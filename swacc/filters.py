#!/usr/bin/env python3

def gen_dict_extract(var, ky):
  if isinstance(var, dict):
    for k, v in var.items():
       if k == ky:
          yield v
       if isinstance(v, (dict,list)):
          yield from gen_dict_extract(v, ky)
  elif isinstance(var, list):
    for d in var:
        yield from gen_dict_extract(d, ky)

def getdictkids(dict1, ky): 
  if not isinstance(dict1, dict):
    yield (ky, dict1)
  else:
    for kd, vl in dict1.items():
      yield from getdictkids(vl, kd)


