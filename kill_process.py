import subprocess
import math
import random
import threading
from time import sleep

def nextTime(rateParameter):
    return -math.log(1.0 - random.random()) / rateParameter

def findPid():
	p1 = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
	p2 = subprocess.Popen(["grep", "spark"], stdin=p1.stdout, stdout=subprocess.PIPE)
	p3 = subprocess.Popen(["grep", "-v", "grep"], stdin=p2.stdout, stdout=subprocess.PIPE)
	(output, err) = p3.communicate()
	list1 = output.split("\n")
	list2 = list1[0].split()
	if len(list2) < 2:
		return 0
	pid = list2[1]
	return pid

def killProcess(pid, times):
	time = nextTime(10)
	sleep(5.0)
	if findPid() == pid:
		subprocess.call(["kill", "-9", str(pid)])
		print "killed process " + str(pid) + " " + str(times) + " times"
		killProcess.check_call(pid, times + 1)

killProcess(findPid(), 1)
# kill -0