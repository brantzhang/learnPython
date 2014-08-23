#!/usr/bin/python
#Filename:backup_ver1.py

import os
import time

#1.The files and directories to be backed up are specified in a list.
source=['/home/jing/3','/home/jing/test1']

#2.The backup must be stored in a main backup directory
target_dir='/home/jing/test2/'

#3.The files are backed up into a zip file.
#4.The current day is the name of the subdirectory in the main directory
today = target_dir +time.strftime('%Y%m%d')
#The current time is the name of zip archive
now = time.strftime('%H%M%S')

#Take a commit from the user to create the name of the zip file
comment = raw_input('Please input a comment -->')
if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_'+comment.replace(' ','_')+'.zip'

#Create the subdirectory if it isn't already there
if not os.path.exists(today):
	os.mkdir(today)
	print "Successfully created directory",today

#6.We use the zip command to put files in a zip archive
zip_command="zip -qr %s %s" %(target,' '.join(source))

#7.Run the backup
if os.system(zip_command)==0:
	print 'Successfule backup to',target
else:
	print 'Backup Failed'
