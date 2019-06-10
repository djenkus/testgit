#!/usr/bin/python
import Queue
import os
import sys
import threading
import time
import datetime
import logging
from subprocess import Popen, PIPE
from current_sensor import *
import os.path
from freqScaling import *
import csv



def freq(*args):
	
	for i in args:
		print(i)
	
	
freq(5, 1,2)	
