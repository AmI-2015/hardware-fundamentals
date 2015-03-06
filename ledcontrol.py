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
    
    #iterate 10 times
    for i in range(10):
        #set the output at 1, LED on
        GPIO.output(15,1)
        # keep it for 1 second 
        time.sleep(1) 
        # set the output at 0, LED off
        GPIO.output(15,0)
        #keep it for 1 second 
        time.sleep(1) 


if __name__ == '__main__':
    main()
    