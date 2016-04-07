import subprocess
#from socket import getaddrinfo
from pprint import pprint

hostsFile = open('hosts.txt', 'r')
hosts = hostsFile.readlines()
passed = []
failed = []
loss = '100% packet loss'

for host in hosts:
  out=error=''
  #result = getaddrinfo(host.rstrip(), None) 
  ''' '''
  args = ['ping','-c','1','-w','2', host.rstrip()] 
  ping = subprocess.Popen(args,stdout = subprocess.PIPE,stderr = subprocess.PIPE)
  out, error = ping.communicate()
  #print  len(error), len(out), out
  if (loss in out) or (len(out) == 0 and len(error) != 0):
    failed.append(host.rstrip())
  else: 
    passed.append(host.rstrip())

print 'succcess : ', len(passed)
pprint(passed)
print 'failed : ', len(failed) 
pprint(failed)
