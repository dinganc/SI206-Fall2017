import re
f=open('mbox-short.txt','r')
for line in f:
    if line.find('From')>=0:
            print(line)
            try:print (''.join((re.findall('([0-9]*)',line))))
            except:pass
            try:print (re.findall('^From: (.*)@',line)[0])
            except:pass
