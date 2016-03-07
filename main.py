import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)

count=1
intensity=1

def button_pressed(channel):
    global count
    if count>4:
	count=0
    if count==4:
   	count+=1
        fade(0,0,1,1,.01)
       	print "ALL BLUE"
    if count==3:
        count+=1
        print "ALL GREEN"   
	fade(0,1,0,1,.01)
    if count==2:
        count+=1
        print "ALL RED"
	fade(1,0,0,1,.01)
    if count==1:
	count+=1
	print "ALL ON"
        sleep(1,1,1,1,.01)

    if count==0:
	count+=1
        fade(0,0,0,1,.01)
	print "OFF"

def sleep(red,green,blue,time_up,fade_time):
	time.sleep(20)

def fade(red,green,blue,time_up,fade_time):

        wait_time=(float(time_up)*60)
        seconds=(float(fade_time)*60)  #calculat seconds based on minutes gived
        maxtime=(seconds/1000) #calculate time to sleep based on minutes given

        os.system("echo 18=0 > /dev/pi-blaster")  # set all to sero
        os.system("echo 23=0 > /dev/pi-blaster")
        os.system("echo 24=0 > /dev/pi-blaster")
        os.system("echo 18="+str(red)+" > /dev/pi-blaster")
        os.system("echo 23="+str(green)+" > /dev/pi-blaster")
        os.system("echo 24="+str(blue)+" > /dev/pi-blaster")

        print "Waiting for "+str(wait_time)+" seconds."
#        time.sleep(float(wait_time))
        time.sleep(5)


#        for i in range(0,1000):
#               while (red>.003):       #to keep it from going under 0, to be safe
#                      red-=.001       #fade away at 1/1000
#		        os.system("echo 18="+str(red)+" > /dev/pi-blaster")
#		while (green>.003):       #to keep it from going under 0, to be safe
#                        green-=.001       #fade away at 1/1000
#                        os.system("echo 18="+str(green)+" > /dev/pi-blaster")
#	os.system("echo 18=0 > /dev/pi-blaster")
#        os.system("echo 23=0 > /dev/pi-blaster")
#        os.system("echo 24=0 > /dev/pi-blaster")

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(17, GPIO.FALLING, callback=button_pressed, bouncetime=300)


try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
