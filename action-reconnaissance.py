#!/usr/bin/env python2
from hermes_python.hermes import Hermes
from datetime import datetime
from pytz import timezone
import random

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):

	print()
	print(intent_message.intent.intent_name)
	print ()



	if intent_message.intent.intent_name == 'xrobquin:Reconnaissance_proche':
		
		liste_reponses_appetit = [", J'adore ce haut"]
		
		sentence = 'Salut '	
		
		if len(intent_message.slots.Name)==1:
			name = intent_message.slots.Name.first().value
			if (name =='William'):
				name = 'Williame'
			    
			sentence += name
			sentence += liste_reponses_appetit[0]
			sentence += str(random.randint(0,10))
			
			    
			
			
		if len(intent_message.slots.Name2)==1:
			sentence += ' et salut '
			name = intent_message.slots.Name2.first().value
			if (name =='William'):
				name = 'Williame'

			
			
				
			
		hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()
	
	
	
	
	
	
	
	
