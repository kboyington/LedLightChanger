import sys
import time
import os
import atexit
import psutil

pid = str(os.getpid())
pidfile = "/tmp/fade.pid"
file(pidfile, 'w').write(pid)

red=(float(sys.argv[1])) #take first command line arg
green=(float(sys.argv[2])) #take first command line arg
blue=(float(sys.argv[3])) #take first command line arg
time_up=(float(sys.argv[4])) #take first command line arg
fade_time=(float(sys.argv[5])) #take first command line arg


def exit_handler():
	print 'My application is ending!'
	intensity=0     #sets it at zero just to kill it
	os.system("echo 18="+str(intensity)+" > /dev/pi-blaster")
	os.system("echo 23="+str(intensity)+" > /dev/pi-blaster")
	os.system("echo 24="+str(intensity)+" > /dev/pi-blaster")


wait_time=(float(time_up)*60)
seconds=(float(fade_time)*60)  #calculat seconds based on minutes gived
maxtime=(seconds/1000) #calculate time to sleep based on minutes given

os.system("echo 18="+str(red)+" > /dev/pi-blaster")
os.system("echo 23="+str(green)+" > /dev/pi-blaster")
os.system("echo 24="+str(blue)+" > /dev/pi-blaster")

print "Waiting for "+str(wait_time)+" seconds."
time.sleep(float(wait_time))

for i in range(0,1000):
	while (red>.003):	#to keep it from going under 0, to be safe
		red-=.001	#fade away at 1/1000 
		os.system("echo 18="+str(red)+" > /dev/pi-blaster")
	while (green>.003):       #to keep it from going under 0, to be safe
                green-=.001       #fade away at 1/1000 
                os.system("echo 23="+str(green)+" > /dev/pi-blaster")
	while (blue>.003):       #to keep it from going under 0, to be safe
                blue-=.001       #fade away at 1/1000 
                os.system("echo 24="+str(blue)+" > /dev/pi-blaster")
	time.sleep(maxtime)	#sleeps the right amount to give 1000 cycles per input amount
#	print i

intensity=0	#sets it at zero just to kill it
os.system("echo 18="+str(intensity)+" > /dev/pi-blaster")
os.system("echo 23="+str(intensity)+" > /dev/pi-blaster")
os.system("echo 24="+str(intensity)+" > /dev/pi-blaster")


os.unlink(pidfile)
#atexit.register(exit_handler)


#with open("history.txt", "a") as myfile:
#    myfile.write(str(intensity)+'\n')
#myfile.close()
