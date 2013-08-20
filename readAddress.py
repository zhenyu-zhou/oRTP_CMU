import sys
import os

# find the path to xia-core
XIADIR=os.getcwd()
while os.path.split(XIADIR)[1] != 'xia-core':
    XIADIR=os.path.split(XIADIR)[0]
sys.path.append(XIADIR + '/api/lib')

from c_xsocket import *

try:
	sock = Xsocket(XSOCK_DGRAM)

	(ad, hid, fid) = XreadLocalHostAddr(sock)

	dag = "%s %s" % (ad, hid)

	print dag

except:
	print "Oops, an error occured."