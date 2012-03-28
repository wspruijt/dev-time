#/usr/bin/env python

import os, sys
import settings
import sqlite3

from time import time

print "Scanning modified files.."

fileList = getFileList(settings.OBSERVE_DIR, time() - settings.SCAN_INTERVAL);

def getFileList(rootdir, from_mtime):

	fileList = []
	
	for root, subFolders, files in os.walk(rootdir):
		
		for file in files:
			f = os.path.join(root,file)		

			if (os.path.getmtime(f) > from_mtime):
				fileList.append(f) 
		
	return fileList;