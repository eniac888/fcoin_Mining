# -*- coding: utf-8 -*-
import os
import time
import subprocess

def readfile(filename):
	f = open(filename,"rb")
	data = f.read()
	return data

while True:
	os.system('tasklist|findstr python>checkProc')
	data = readfile('checkProc')
	if len(data)<80:
		child = subprocess.Popen('procprotect.cmd',shell=True)
	time.sleep(10)
