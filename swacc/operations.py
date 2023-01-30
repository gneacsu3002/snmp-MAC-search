#!/usr/bin/env python3

from swacc import decorators
from pysnmp.hlapi import *

@decorators.applyOP
@decorators.logFnCall
def alive(*args, **kwargs):
  import os
  if not os.system(f"ping -c 1 -w2 {kwargs['ip']} > /dev/null 2>&1"):
      print(f"Host: {kwargs['name']}, is alive!!!")
  else:
      print(f"Host: {kwargs['name']}, is not alive!!!")

@decorators.applyOP
@decorators.logFnCall
def findport(*args, **kwargs):
  OID = '1.3.6.1.2.1.17.4.3.1.2'
  # ex. mac1 = '128.238.115.241.112.25'
  errIn, errStat, errIndx, varBinds = next(
        getCmd(SnmpEngine(),
            CommunityData(kwargs['comunity']),
            UdpTransportTarget((kwargs['ip'], 161)),
            ContextData(),
            ObjectType(ObjectIdentity(OID + '.' + kwargs['MAC'])))
        )

  if errIn:
    print(errIn)
  elif errStat:
    print('%s at %s' % (errStat.prettyPrint(), errIndx and varBinds[int(errIndx) - 1][0] or '?'))
  else:
    for varBind in varBinds:
        port = [x.prettyPrint() for x in varBind]
        # port = varBind[0].split("=")
        if "No Such" in port[1]:
          port = "device not known"
        else:
          port = f" port {port[1]}"
        print(f"sw: {kwargs['ip']} = {port}")
        # print(' = '.join([x.prettyPrint() for x in varBind]))

@decorators.applyOP
@decorators.decoDbg
def rebootpi(*args, **kwargs):
  import os
  user = 'pi'
  password = 'rasp'

  if not os.system(f"ruby pisshcmd.rb {user} {kwargs['ip']} {password} 'sudo reboot' &"):
    print(f"{kwargs['name']}: reboot {user}@{kwargs['ip']} &")
  else:
    print(f'''Target machine: {kwargs['name']} , cannot be rebooted !!!''')

@decorators.applyOP
@decorators.decoDbg
def ssh(*args, **kwargs):
  import os
  user = 'pi'
  password = 'raspberry'
  
  if not os.system(f"ssh -y {user}@{kwargs['ip']} &"):
    print(f"{kwargs['name']}: ssh {user}@{kwargs['ip']} &")
  else:
    print(f'''Cannot SSH on target machine: {kwargs['name']} !!!''')

def main():
    print(dir())
    
if __name__ == '__main__':
    main()

