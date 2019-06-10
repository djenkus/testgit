
#!/usr/bin/python

##!/usr/bin/env python


import sys
import os
import datetime
import time
import logging
import subprocess

import json
from collections import OrderedDict
import os.path
import argparse
parser = argparse.ArgumentParser()


parser.add_argument('-fb', action='store', dest='freqB',
                    help='To set frequency of big cores')
parser.add_argument('-fl', action='store', dest='freqL',
                    help='To set frequency of little cores')

args = parser.parse_args()

FCONFIG_PATH = os.path.abspath(os.path.join(__file__, "../")) + "/freqConfig.json"
#, "/freqConfig.json")
print(FCONFIG_PATH)

with open(FCONFIG_PATH) as f:
  freqConfig = json.load(f, object_pairs_hook=OrderedDict)

# CPUfreq directory
CPU_FREQ_PATH = freqConfig['CPUFREQ']['PATH']

# To store config data about CPUs
CPUlist =  OrderedDict({})
cmd_FREQ = [None] * 2
clusters_freq = [None] * 2

for cpus in freqConfig['CPU']:
	CPUlist[cpus] = {}
	for fields in freqConfig['CPU'][cpus]:
		CPUlist[cpus][fields] = freqConfig['CPU'][cpus][fields]

cmd_set_GOVERNOR = []
cmd_set_FREQ = []
cmd_check_current_freq = []
cmd_print_available_freq = []
cmd_print_governor = []

# define cmd commands
for cpus in CPUlist:
	cmd_set_GOVERNOR.append("echo userspace > " + CPU_FREQ_PATH + CPUlist[cpus]['PATH'] + CPUlist[cpus]['GOVERNOR'])
	cmd_set_FREQ.append("echo  > " +  CPU_FREQ_PATH + CPUlist[cpus]['PATH'] + CPUlist[cpus]['SET_FREQ'])
	cmd_check_current_freq.append(CPU_FREQ_PATH + CPUlist[cpus]['PATH'] + CPUlist[cpus]['CURRENT_FREQ'])
	cmd_print_available_freq.append(CPU_FREQ_PATH + CPUlist[cpus]['PATH'] + CPUlist[cpus]['FREQ_LIST']) 
	cmd_print_governor.append(CPU_FREQ_PATH + CPUlist[cpus]['PATH'] + CPUlist[cpus]['GOVERNOR'])
		

temp_log_file = 'logfile.txt'

#configure logging
#logging.basicConfig(level=logging.DEBUG)
#logger = logging.getLogger(__name__ + '.run_workloads')


def check_current_freq():
	check_string =[]
	for cpus in range(0, len(CPUlist)):
		check_string.append(str(subprocess.check_output(["cat", cmd_check_current_freq[cpus]])))
	check_string = map(lambda s: s.strip(), check_string)
	return check_string

def print_available_freq():
	f_list, check_string =[], []
	for cpus in range(0, len(CPUlist)):
		check_string.append(str(subprocess.check_output(["cat", cmd_print_available_freq[cpus]])))
	for freqs in range(0, len(check_string)):
		f_list.append(check_string[freqs].split())
	return  f_list

def print_governor():
	check_string = []
	for cpus in range(0, len(CPUlist)):
		check_string.append(str(subprocess.check_output(["cat", cmd_print_governor[cpus]])))
	check_string = map(lambda s: s.strip(), check_string)
	return check_string



def set_freq(*cluster_MHz, **cluster_select):

	
	for clusterNum in range(0, len(cluster_MHz)):
		clusters_freq[clusterNum] = cluster_MHz[clusterNum]
	
	if __name__ == '__main__':
		clusters_freq[0] *= 1000
		clusters_freq[1] *= 1000	
		
	
	if cluster_select['cluster'] == "both" and len(cluster_MHz) == 2:
		# set userspace governor
		subprocess.call(cmd_set_GOVERNOR[0], shell = True)  
		subprocess.call(cmd_set_GOVERNOR[1], shell = True)
		
		cmd_FREQ[0] = cmd_set_FREQ[0][:5] + str(clusters_freq[0]) + cmd_set_FREQ[0][5:]
		cmd_FREQ[1] = cmd_set_FREQ[1][:5] + str(clusters_freq[1]) + cmd_set_FREQ[1][5:]
		
		# set frequency for both clusters	
		subprocess.call(cmd_FREQ[0], shell = True)
		subprocess.call(cmd_FREQ[1], shell = True)
		
	elif cluster_select['cluster'] == "0" or cluster_select['cluster'] == "1":
		
		clstr = int(cluster_select['cluster'])
		# set userspace governor for a selected cluster
		subprocess.call(cmd_set_GOVERNOR[clstr], shell = True)
		# set frequency for a selected cluster
		cmd_FREQ[clstr] = cmd_set_FREQ[clstr][:5] + str(clusters_freq[clstr]) + cmd_set_FREQ[clstr][5:]
 		subprocess.call(cmd_FREQ[clstr], shell = True)


def set_frequency(A53_MHz, A57_MHz):
	logging.debug('Setting frequency: ' + str(A53_MHz) + ', ' + str(A57_MHz))
	subprocess.call(["cpufreq-set", "-c", "0", "-g", "userspace" ])	
	subprocess.call(["cpufreq-set", "-c", "4", "-g", "userspace" ])	

	subprocess.call(["cpufreq-set", "-c", "0", "-f", str(A53_MHz) + 'Mhz' ])	
	subprocess.call(["cpufreq-set", "-c", "4", "-f", str(A57_MHz) + 'Mhz' ])	








if __name__ == '__main__':


	selected_big_f = int(args.freqB)
	selected_little_f = int(args.freqL)		
	#print(selected_little_f)
	#print(selected_big_f)

	set_freq(selected_little_f, selected_big_f, cluster = "both")
	
	print(check_current_freq())
	print(print_available_freq())
	print(print_governor())


