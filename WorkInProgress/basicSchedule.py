import datetime
import time

def convert24 ():
	h24 = datetime.datetime.now().hour
	if h24 >12:
		h24 = h24-12
	return h24

def addZero ():
	minStart = datetime.datetime.now().minute
	if minStart < 10:
		minStart = '0' + str(minStart)
	return minStart

while 1:
	hourNow = convert24()
	minNow = addZero()
	#hourNow = 10
	#minNow = 17
	print ("The time is: ",hourNow,minNow)
	#time.sleep(30)
	time.sleep(60)

# Class times
	if hourNow==11 and minNow==56:
		print("Almost noon")
	if hourNow==12 and minNow==5:
		print("It is now after noon")
	if hourNow==1 and minNow==30:
		print("Middle of the afternoon")
	if hourNow==3 and minNow==00:
		print("One hour to go")
	print ("looooop")
