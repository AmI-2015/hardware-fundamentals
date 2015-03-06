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


def main(): 
    # set the board numbering mode
    GPIO.setmode(GPIO.BOARD)
     # set-up pin function
    GPIO.setup(15,GPIO.OUT)
    
    #infinite cycle
    while True:
        #time measuring routine
        rc = RCtime(13)
        
        #debug
        print rc
        
        # if the RC count is lower than a give threshold,
        # light the led up, otherwise turn it off
        if rc < 2000:
            GPIO.output(15,GPIO.LOW)
        else:
            GPIO.output(15,GPIO.HIGH)
    
def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.setup(RCpin, GPIO.IN)
    
    # This takes about 1 millisecond per loop cycle
    start = time.time()
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    print (time.time()-start)*1000.0, "ms"
    return reading


if __name__ == '__main__':
    main()