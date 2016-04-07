import paramiko
import time
import select
import getpass
from pprint import pprint
import StringIO

switchname=raw_input('give SW name: ')
#print switchname
if len(switchname) < 1:
    print 'please enter a valid device name'
    exit(1)
myuser=raw_input('Username: ')
mypass=getpass.getpass('Password:')

def read_buffer(chan):
    while not chan.exit_status_ready():
        if chan.recv_ready():
            contents = ""
            data = chan.recv(2048)
            #print data
            while data:
                contents += data
                data = chan.recv(1024)
    return contents

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(switchname ,  username=myuser ,  password=mypass, timeout=25)
channel = ssh.get_transport().open_session()
channel.exec_command("show vrrp")
output = read_buffer(channel)
#output = channel.recv(1024)
print output
print type(output)
#ssh.close()
outlines = output.split('\n')
count = 0
lcount = 2
vrrp_info = {}
for line in outlines:
    count += 1
    #print line,'\n'
    if 'Vlan' in line:
        vl = line.split()
        vrrp_info[vl[0]] = {}
        vrrp_info[vl[0]]['vrrp group'] = vl[1]
        vrrp_info[vl[0]]['priority'] = vl[3]
        vrrp_info[vl[0]]['preempt'] = vl[6]
        vrrp_info[vl[0]]['state'] = vl[7]
        vrrp_info[vl[0]]['vrip'] = vl[8]

pprint(vrrp_info)
print count
