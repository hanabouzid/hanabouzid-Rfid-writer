from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft import MycroftSkill, intent_file_handler
import json
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

class RfidWriter(MycroftSkill):

    def __init__(self):
        super(RfidWriter, self).__init__(name="RfidWtiter")
        

    @intent_handler(IntentBuilder("").require("query"))
    def handle_login(self):
        try:
            test = self.get_response('what\'s the full name of the employee')
            t = "Ahmed Fouratti"
            self.speak("Now place your tag on the reader to write the information you added")
            reader.write(t)
            self.speak_dialog("writing.successful", data={'name': t})
        finally:
            GPIO.cleanup()

def create_skill():
    return RfidWriter()
