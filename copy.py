import shutil
import os
import time
print time.time()
#print "didnt error"
source = 'C:\Users\matthew.louque\Test'#'D:\postilion\Trace\Bankway\Bankway'
destinationPrefix = 'C:\Users\matthew.louque\TestDestination'#'C:\Users\Administrator\Desktop\TraceFiles\Trace'
destinationSuffix = 1
destination = destinationPrefix + str(destinationSuffix)
#print destination
targetSize = 48000
previousSize = 0
TIME_INTERVAL = 15
timeForNextScan=0
#shutil.copytree(source, destination)


'''
def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size

print "Size: " + str(getFolderSize("."))
'''

def get_size(start_path = 'D:\postilion\Trace\Bankway\Bankway'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

while (True):
	if ((time.time()>= timeForNextScan)): #and(get_size() >= targetSize) and  and (get_size() != previousSize)):
		print "copying files"
		#previousSize = get_size()
		shutil.copytree(source, destination)
		print "files copied"
		destinationSuffix += 1
		destination = destinationPrefix + str(destinationSuffix)
		timeForNextScan = time.time()+ TIME_INTERVAL
		
print get_size()
