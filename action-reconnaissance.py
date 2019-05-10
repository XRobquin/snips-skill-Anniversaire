#!/usr/bin/env python2
from hermes_python.hermes import Hermes
from datetime import datetime
from pytz import timezone

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):

	print()
	print(intent_message.intent.intent_name)
	print ()

	if intent_message.intent.intent_name == 'xrobquin:Reconnaissance_proche':
		
		sentence = 'Salut '		
		if len(intent_message.slots.Name)==1:
			#name = 'toi'
			name = intent_message.slots.Name.first().value
			sentence += name
			print(sentence)
			
				
			
		hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()
	
	
	
	
	
	
	
	
