import RPi.GPIO as GPIO
import time
import urllib2
import json

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(16, GPIO.IN)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.output(18, 0)
GPIO.output(21, 0)
GPIO.output(26, 0)

url = 'http://127.0.0.1:5000/createOrder'

try:
	while True:
		input_state_4 = GPIO.input(4)
		input_state_12 = GPIO.input(12)	
		input_state_16 = GPIO.input(16)
		
	        #Shop flags to warehouse to order more inventory
		if input_state_4 == True:

			#Warehouse light on to order more inventory
			GPIO.output(18, 1)

			#Shop light on to flag order has been requested
			GPIO.output(26, 1)

			#Create an order
			parameters = {'partNumber': '123456'}
                        data = json.dumps(parameters)

                        req = urllib2.Request(url, data)
                        req.add_header('Content-Type', 'application/json')
                        
                        response = urllib2.urlopen(req)

                        responseData = json.load(response)
                        print(responseData['returnObject']['message'])

                        time.sleep(1)

		#Order has been created by warehouse
		if input_state_12 == True:

			#Warehouse light off to order more inventory
			GPIO.output(18, 0)

			#Warehouse light on to see shop receiving of inventory
			GPIO.output(21, 1)

		#Order has been received by shop
		if input_state_16 == True:

			#Warehouse light off to see shop receiveing of inventory
			GPIO.output(21, 0)

			#Shop light off for inventory received
			GPIO.output(26, 0)

except KeyboardInterrupt:
	GPIO.cleanup()
