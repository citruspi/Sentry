#! /usr/bin/python

#################################################################
# Script      = Sentry
# Version     = v0.1
# Author      = Mihir Singh (@citruspi)
# Description = Sends Papertrail alerts as SMS's via Twilio
#################################################################

import os
import json
from flask import Flask, request
from twilio.rest import TwilioRestClient

app = Flask(__name__)

########################################## Twilio Settings ##########################################
account_sid  = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"		# Twilio Account SID
auth_token   = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"		# Twilio Account Authentication Token
phone_number = "+1XXXXXXXXXX"							# Phone number to send the alert to
from_number  = "+1XXXXXXXXXX" 							# Number purchased with Twilio

# Possible Event Data (to Construct Custom Message)
# - id
# - received_at
# - generated_at
# - source_name
# - source_ip
# - facility
# - severity
# - program
# - message

@app.route('/')
def hello():
    return 'Welcome to Sentry.' #In case someone stumbles upon the address

@app.route('/sentry', methods=['POST']) #Set Webhook URL to this
def sentry():
	if request.method == 'POST': #If its a POST Request...
		
		client = TwilioRestClient(account_sid, auth_token) #Create a new Twilio Client

		jsonstr = json.loads(request.form['payload']) #Load the Payload (Papertrail events)

		for event in jsonstr['events']: #Iterate through events
			
			message = "(" + event["display_received_at"] + ")" + " " + event["source_name"] + " " + event["program"] + " | " + event["message"] #Construct the message

			parts = [message[i:i+160] for i in range(0, len(message), 160)] #Split it into 160 character messages (character limit on SMS's)

			for part in parts: #Iterate through each 160 character part
				sent = client.sms.messages.create(to=phone_number, from_=from_number, body=part) #Send it via Twilio

	return "Panda Bears Are Awesome!" #Simply for the sake of returning something

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)