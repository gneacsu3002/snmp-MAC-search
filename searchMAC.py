#!/usr/bin/env python3

from pprint import pprint
import sys
from swacc import operations, comunity, MAC

def main():
  if (len(sys.argv) > 3):
    devtp = sys.argv[1]
    oper = sys.argv[2]
    location = sys.argv[3]

    if ((devtp != 'sw') and (devtp != 'iot') and (devtp != 'pc')):
        print(' Device type is not valid ')
        sys.exit(2)
    if ((oper != 'reboot') and (oper != 'ping') and (oper != 'search') and (oper != 'ssh') and (oper != 'findport')):
        print(' Unknown operation ')
        sys.exit(2)
  else:
    print('Program needs a device category and location as argument !!!')
    sys.exit(2) 

  if (devtp == 'sw'):
    ymlfile = 'sw.yml'
  elif (devtp == 'iot'):
    ymlfile = 'iot.yml'
  else:
    ymlfile = 'pc.yml'

  if (oper == 'ping'):
    operations.alive(ymlfile=ymlfile, location=location)
  elif (oper == 'reboot'):
    operations.rebootpi(ymlfile=ymlfile, location=location)
  elif (oper == 'ssh'):
    operations.ssh(ymlfile=ymlfile, location=location)
  elif (oper == 'findport'):
    # ex. macstr = "778e2c441d3a"
    macstr = sys.argv[4]
    if (len(sys.argv) > 5):
      macstr = sys.argv[5]
      comunity = sys.argv[4]
  
    splt_str = []
    if (len(macstr) == 12):
      for idx in range(0, len(macstr), 2):
        splt_str.append(macstr[idx: idx + 2])
      MAC = '.'.join([str(int(a,16)) for a in splt_str])
    else:
      print(' MAC address is not valid ')
      sys.exit(2)
    
    operations.findport(ymlfile=ymlfile, location=location, MAC=MAC, comunity=comunity)
  elif (oper == 'search'):
    for yt in swacc.filters.gen_dict_extract(ymlparsed['all'], location):
      pprint(yt)
  else:
    print('Command not found !!!')

if __name__ == "__main__":
    main()

