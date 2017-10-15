#!/usr/bin/env python
# -*- coding: utf-8 -*-



import time
import os
import sys
from pyfingerprint.pyfingerprint import PyFingerprint
from getContacts import doFinger
from subprocess import Popen, check_call, PIPE
from carefullyLoadYaml import *

faceBoolPath = "isFaceBool.yml"
## Search for a finger
##

## Tries to initialize the sensor
def setupSensor():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')
    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        raise(Exception)
    return(f)

## Gets some sensor information
#print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

def waitForFingerLift(f):
    while ( f.readImage() == True ):
        time.sleep(1);
        

def multiTestFinger(f, tries = 5):
    while (tries>0):
        time.sleep(0.2)
        try:
            result = testFinger(f)
        except Exception as e:
            pass
        else:
            positionNumber = result[0]
            accuracyScore = result[1]
            if ( positionNumber == -1 ):
                print('Please lift and replace finger. Finger not recognized.')
                waitForFingerLift(f)
            else:
                print('Found template at position #' + str(positionNumber))
                print('The accuracy score is: ' + str(accuracyScore))
            return(result)
            tries -=1;

def testFinger(f):
    
    ## Tries to search the finger and calculate hash
    result = [-1, -1]
    try:
        print('Waiting for finger...')
        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass
        print ('Got Finger')
        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

        ## Searchs template
        result = f.searchTemplate()



    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        raise
    return(result)
#    exit(1)

def execChrome(url):
    pid = os.fork()
    if pid == 0:
        os.execv('/usr/bin/chromium-browser', ('--enable-consumer-kiosk', url))
        exit(1)
    return(pid)

def waitForEnd(f):
    faceInScreen = True
    while faceInScreen:
        try:
            print("opening ipython for faceDetector")
            faceInScreen = Popen(['ipython', '/home/pi/Documents/Grandma/faceDetector2.py'], stdout=PIPE)
        except Exception as e:
            print("Process Popen or comunication or killing error. Exception:", e)
        try:
            if f.readImage():
                return(True)
        except Exception as e:
            print('f.readImage communication error. Exception: ', e)
        time.sleep(10)
    
    print('Terminating this call in 30 seconds, face the camera to continue call')
    for i in range(0, 30):
        if faceInScreen:
            waitForEnd(f)
            break;
        time.sleep(1)
    

def sendMessage(mf, url):
    try:
        doFinger(mf[0], url)
    except KeyError as ke:
        print('data base was missing finger', file=sys.stderr)
    except Exception as e:
        print('undefined data base or smtp error: '+e, file=sys.stderr)
    else:
        return(True)
    return(False)

def browserStarted(url):
    try:
        p = Popen(('/usr/bin/chromium-browser', '--kiosk', '--incognito', url))
        print("pid",p.pid)
    except Exception as e:
        print('chrome failed. Exception: ', e)
    else:
        return True
    return False

def killBrowser():
    try:
        check_call(['killall', '-9', 'chromium-browser'])
        pass
    except Exception as e:
        print('killall returned exception: ', e, file=sys.stderr)
    #check_call(('kill', '-3', str(pid)))

def main():
    f = setupSensor()
    while(True):
        mf = multiTestFinger(f)
        if mf[0] != -1:
            url = 'https://appear.in/perryp'
                            #pid = execChrome(url)
            if sendMessage(mf, url):
                if browserStarted(url):
                    waitForFingerLift(f)
                    time.sleep(30)
                    waitForEnd(f)
                    killBrowser()

main()
