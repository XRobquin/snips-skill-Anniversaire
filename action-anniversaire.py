#!/usr/bin/env python2
from hermes_python.hermes import Hermes
import datetime
from pytz import timezone
import random

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))





def intent_received(hermes, intent_message):

	print()
	print(intent_message.intent.intent_name)
	print ()
	
	if intent_message.intent.intent_name == 'xrobquin:question_anniversaire':
		
		if len(intent_message.slots.Name)==0:
			if (name =='William'):
				janniv = 2
				manniv = 6
			if (name =='Marie'):
				janniv = 3
				manniv = 6
			
				
	
		
		else:
			janniv = 1
			manniv = 11


		now = datetime.datetime.now()
		year = now.year
		today = datetime.date.today()
		anniv = datetime.date(year+1, manniv, janniv) 
		diff = anniv - today

		liste_reponses = ["Il reste "+str(diff.days%365-1)+" jours avant votre anniversaire"]			    

		sentence = liste_reponses[random.randint(0,len(liste_reponses)-1)]		
	
			
	
	



		
				
			
		hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()
	
	
	
	
