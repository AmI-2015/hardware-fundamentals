'''
Created on Mar 6, 2015

Copyright 2015 Dario Bonino 
 
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License

@author: bonino
'''

import RPi.GPIO as GPIO
import time

# set the GPIO library in DEBUG mode
DEBUG = 1


def button_to_led (rc_pin):
    # set-up pins
    GPIO.setup(rc_pin, GPIO.IN)
    GPIO.setup(15,GPIO.OUT)
    
    # This takes about 1 millisecond per loop cycle
    #
    # Turn the output pin high (3.3V) if the RCpin input pin goes at ground
    # else turn the output pin at ground (0V)
    # 
    while (True):
        if(GPIO.input(rc_pin) == False):
            GPIO.output(15,GPIO.HIGH)
        else:
            GPIO.output(15,GPIO.LOW)
    return

def main():
    # set the board numbering mode
    GPIO.setmode(GPIO.BOARD)
    
    # start the sampling routine
    button_to_led(11)

if __name__ == '__main__':
    main()