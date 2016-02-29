import sys
emailFile = sys.argv[1]
blacklistFile = sys.argv[2]

f = open(emailFile, "r")
lines = f.readlines()
f.close()
f = open(emailFile, "w")
def deleteContent(emailFile):
	emailFile.seek(0)
	emailFile.truncate()

g = open(blacklistFile, "r")
lines2 = g.readlines()
g.close()

outVal = [word for word in lines if not any(bad in word for bad in lines2)]
for lines3 in outVal:
	f.write(lines3)
	
