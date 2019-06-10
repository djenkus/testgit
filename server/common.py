# cat common.py
#!/usr/bin/python

import os
import sys
import threading
import time
import datetime
from subprocess import Popen, PIPE

def exy_booted(exnr):
    if (exnr > 3 or exnr < 0):
        return False
    addr = '0xb005' + str(exnr) + '000'
    (stdout, stderr) = Popen(["/root/read_physical32 " + addr], stdout=PIPE, shell=True).communicate()
    if(int(stdout, 16) & 2**30):
        return True
    else:
        return False

def nr_exy_booted():
    res = 0
    for i in range(0, 4):
        if(exy_booted(i)):
            res += 1
    
    return res


def exy_poweroff(exnr):
    if (exnr > 3 or exnr < 0):
        return
    
    os.system('echo 0 > /proc/knode/exynos' + str(exnr) + '/run')    


def log(logFile, message):
    os.system('echo "' + message + '" >> ' + logFile)
    os.system("sync")

def pr(message, logFile):
    print(os.path.basename(sys.argv[0]) + ": " + message)
    if ((logFile != None) and (logFile != "")):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M.%S')
        log(logFile, st + " " + message)

def prerr(message, logFile):
    sys.stdout.write(RED)
    pr("Error: " + message, logFile)
    sys.stdout.write(RESET)

def prwarn(srv, message, logFile):
    pr("Warning: " + message, logFile)


def prierr(srv, message, logFile):
    sys.stdout.write(RED)
    pr("Internal Error: " + message, logFile)
    sys.stdout.write(RESET)

