

#!/usr/bin/python
import Queue
import os
import sys
import threading
import time
import datetime
import logging
from subprocess import Popen, PIPE
import csv

file_dir = os.path.dirname(__file__)

#sys.path.append(os.path.join(file_dir, '../../'))


config_path = os.path.abspath(os.path.join(__file__ ,"../.."))
sys.path.insert(0, config_path)

print(config_path)
from config import *


print("----------")
for k in sys.path:
        print k
print("..........")



#FREQ_CONFIG_PATH = os.getcwd()
#sys.path.insert(0, 'path/to/your/py_file')

#path_power_log = "/root/pacl/power_monitor.log"

#logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s', filename = path_power_log)


f_list = print_available_freq()
samples = 10




def logPower(logFile, message):
    os.system('echo "' + message + '" >> ' + logFile)
    os.system("sync")


class PowerProfiler():

	samples = 10
	cluster0_flist = []
	cluster1_flist = []

	def __init__(self, freqList, **kwargs):
		
		self.freqList = freqList
		self.cpu_clusters = kwargs['cpu_clusters']
		

		if self.cpu_clusters == 1:
			PowerProfiler.cluster0_flist = self.freqList
		elif self.cpu_clusters == 2:
			PowerProfiler.cluster0_flist = self.freqList[0]
			PowerProfiler.cluster1_flist = self.freqList[1]
			self.prepare_f_list()


 	def prepare_f_list(self):
		# expand frequency list to match
		if self.cpu_clusters == 2:
			if len(self.cluster0_flist) < len(self.cluster1_flist):
				for i in range(len(self.cluster0_flist), len(self.cluster1_flist)):
					self.cluster0_flist.append(self.cluster0_flist[-1])   
			elif len(self.cluster1_flist) < len(self.cluster0_flist):
				for i in range(len(self.cluster1_flist), len(self.cluster0_flist)):
					self.cluster1_flist.append(self.cluster1_flist[-1])	


	def start_idle_profiler(self, **exynosNum):
		
		self.exynosAvailable = exynosNum['exynos']
		
		print("running")
		my_queue = Queue.Queue()
		idleThread = threading.Thread(target=self.idle_power, args=(my_queue, self.exynosAvailable,))
		idleThread.start()
		idleThread.join()
		func_value = my_queue.get()
		#print func_value
	

	def estimate_idle():
		pass

	def idle_power(self, out_queue, exynosON):
	
		
		save_path = os.getcwd() + "/" + "idle_power_exynos_" + str(exynosON) + ".csv"
		print(save_path)
		
		# delete file if exists
		if os.path.exists(save_path):
			os.remove(save_path)
			
		
		if self.cpu_clusters == 1:
		
			average_idle =[]
				
 			for freqs in range(0, len(self.cluster0_flist)):
 				powerSum = 0	
 				#set frequencies, little cores set at max
				set_freq(self.cluster1_flist[freqs], self.cluster0_flist[15], cluster="both")
				time.sleep(0.1)
				for samp in range(0, samples):
					powerSum += get_power()
					print(get_power())		

				average_idle.append(powerSum/samples)
				#print(average_idle[freqs])
				print(check_current_freq())

			header = ['Frequency (Mhz)'] + self.cluster0_flist

			with open(save_path, 'w') as csvFile:
   		 		writer = csv.writer(csvFile)
    			writer.writerow(header)
    			writer.writerows(average_idle)
	
		
		elif self.cpu_clusters ==2:
			
		    #2d list to save average power 
			average_idle = [[] for i in range(len(self.cluster1_flist))]
		
			header = ['Frequency (Mhz)'] + self.cluster1_flist 
		
			
			for f in range(0, len(self.cluster0_flist)):
				for freqs in range(0, len(self.cluster1_flist)):
					powerSum = 0	
					#set frequencies, little cores set at max
					set_freq(self.cluster0_flist[f], self.cluster1_flist[freqs], cluster="both")
					time.sleep(0.1)
					for samp in range(0, samples):
						powerSum += float( get_power())
						print(get_power())		

					average_idle[f].append(powerSum/samples)
					print(check_current_freq())
				print(average_idle)
			with open(save_path, 'w') as csvFile:
				writer = csv.writer(csvFile)
				writer.writerow(header)
				for dat in range(0,len(self.cluster1_flist)):
					plist = average_idle[dat]
					plist.insert(0, self.cluster0_flist[dat])
					writer.writerow(plist)

		out_queue.put(average_idle)
		

def main():

	profiler = PowerProfiler(f_list, cpu_clusters = 2)
	profiler.start_idle_profiler(exynos = 1) 







if __name__ == '__main__':
	main()




