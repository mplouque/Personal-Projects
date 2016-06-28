import shutil
import os
import time
#print time.time()
#print "didnt error"

#the source and destination must be a string, including the drive letter
source = 'C:\Users\matthew.louque\Test'#'D:\postilion\Trace\Bankway\Bankway'
destinationPrefix = 'C:\Users\matthew.louque\TestDestination'#'C:\Users\Administrator\Desktop\TraceFiles\Trace'
destinationSuffix = 1
#combine the prefix and suffix to create a file name that changes everytime the folder is copied
destination = destinationPrefix + str(destinationSuffix)
#print destination

#target size in bytes
targetSize = 48000*1024
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

#function that looks at the size of the target directory
#also looks recursively for all sub directories
def get_size(start_path = 'D:\postilion\Trace\Bankway\Bankway'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

#loop forever
while (True):
	#if the size is large enoguh and a copy hasnt been done within the time interval
	if ((time.time()>= timeForNextScan) and (get_size() >= targetSize) and (get_size() != previousSize)):
		print "copying files"
		#previousSize = get_size()
		shutil.copytree(source, destination)
		print "files copied"
		#change the name of the next destination file
		#The name must not already exist
		destinationSuffix += 1
		destination = destinationPrefix + str(destinationSuffix)
		#Wait X amount of time before doing another scan 
		timeForNextScan = time.time()+ TIME_INTERVAL
		
