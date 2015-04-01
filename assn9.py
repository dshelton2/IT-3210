import csv

#records = []
dictlist = []
with open('netlog.csv', 'r') as f:
	csvObj = csv.reader(f)
	header = next(csvObj)
	#records.append(header)
	'''
	-- read each record into a dictionary, then create a list with these dictionaries
	'''	
	for row in csvObj:
		dictlist.append(dict(zip(header, row)))
		#records.append(row)

'''
-- place all of the source and destination addresses in separate lists and identify
any addresses that occur in both lists --
I Changed one IP to validate that multiple matches would display properly, test if you like.
https://docs.python.org/2/library/sets.html
http://stackoverflow.com/questions/18453566/python-dictionary-get-list-of-values-for-list-of-keys
'''
		
srcAdd = [d['Src Addr'] for d in dictlist]
dstAdd = [d['Dst Addr'] for d in dictlist]
compare = set(srcAdd) & set(dstAdd)
matches = []
for x in compare:
	matches.append(x)
print "IPs occurring in both source and destination: %s" % ", ".join(i for i in matches)

TCPUDPlist = [d['Protocol'] for d in dictlist]

TCP = 0
UDP = 0

for x in TCPUDPlist:
	if x == 'TCP':
		TCP += 1
	elif x == 'UDP':
		UDP += 1
	else:
		print "Protocol Error"
		
print '\nUDP | TCP'
print '-' * 9 
print '%3d | %3d' % (UDP, TCP)
