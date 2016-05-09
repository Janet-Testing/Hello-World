#!/usr/bin/env monkeyrunner
# This script is for test
# Launch camera->clicking shutter button->capture screen->back to home
import time
import os
import sys
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By


# -- START: User defined variable -- #
iShutterTimes = 1
# -- End: User defined variable -- #


# -- START: Constant values -- #
SHORT_TIME = 1
LONG_TIME = 4
sProjectPath = "C:/WorkItems/MonkeyRunner/Alex/"
CaseID = 'None'
iLOOPTIMES = 1000000
DEBUG = 0
# -- END: Constant values -- #


# ----------START: User defined functions---------- #

# 
# Initlize test environment
# Push the test resource into /data/
#
def setUp():
    
    sleep(SHORT_TIME)
    backToHome()

#   
# Clean test environment
# Remove test resource from DUT
#
def tearDown():
    sleep(SHORT_TIME)
    backToHome()
    
#
# Process test steps for M370_pfp_0014
#
def processTestCase(iLoop):
	setUp()
        launchDown()

#	launchCamera()
#	ClickShutter(iShutterTimes)
#	ClickSettings(iShutterTimes)
#   ClickWBSettings(iLoop%5)
#   ChangeToVideoMode()
#   ChangeToPhotoMode()
#   ClickShutter(iShutterTimes)
	tearDown()

def launchDown():
    device.touch(1137,1140,"DOWN_AND_UP")
    sleep(SHORT_TIME);
	
def ClickShutter(times):
    print "ClickShutter"
    for i in range (0,times):
        device.touch(1198,370,"DOWN_AND_UP")
        sleep(SHORT_TIME)
    
def ClickSettings(times):
    print "ClickSettings"
    for i in range (0,times):
        device.touch(305,509,"DOWN_AND_UP")
        sleep(SHORT_TIME)    
    
def ClickSettings_ChangeSizeToLeft():
    print "ClickSettings_ChangeSizeToLeft"
    ClickSettings(1)
    device.touch(320,590,"DOWN_AND_UP")
    sleep(SHORT_TIME)  
    
def ClickSettings_ChangeSizeToRight():
    print "ClickSettings_ChangeSizeToRight"
    ClickSettings(1)
    device.touch(440,590,"DOWN_AND_UP")
    sleep(SHORT_TIME)      

def ClickSettings_ChangeFaceDetecting():
    print "ClickSettings_ChangeFaceDetecting"
    ClickSettings(1)
    device.touch(400,630,"DOWN_AND_UP")
    sleep(SHORT_TIME)

def ChangeToVideoMode():
    print "Change to Video mode"
    device.touch(40,920,"DOWN_AND_UP")
    sleep(SHORT_TIME)
    
def ChangeToPhotoMode():
    print "Change to Photo mode"
    device.touch(40,850,"DOWN_AND_UP")
    sleep(SHORT_TIME)
    
def ClickWBSettings(item):
    print "Change White Balance Mode %i" %(item+1)
    wb_x = 280
    wb_y = (item)*50 + 470
    ClickSettings(1)
    device.touch(120,770,"DOWN_AND_UP")
    sleep(SHORT_TIME)
    device.touch(wb_x,wb_y,"DOWN_AND_UP")
    print "X = %i, Y = %i" %(wb_x,wb_y)
    sleep(SHORT_TIME)

def launchCamera():
    # Launch Camera;
    print "Launch Camera..."
    device.shell('am start -a android.intent.action.MAIN -n com.android.gallery3d/com.android.camera.CameraLauncher')
    sleep(2)
# ----------END: User defined functions---------- #


# ----------START: Common functions---------- #
def getDevice():
    # Get current device
    device = MonkeyRunner.waitForConnection()
    if not device:
        print "Error: Device is NOT connected!"
        sys.exit()
    else:
        print "Device is connected...OK"
        return device

def getEasyDevice():
    # Get easy_device
    easy_device = EasyMonkeyDevice(device)
    print "EasyMonkeyDevice is initlized...OK"
    return easy_device

def sleep(TIME):
    MonkeyRunner.sleep(TIME)

def unlockDev():
    print "Wake and unlock device..."
    device.wake()
    sleep(SHORT_TIME)
    device.drag((360,1050),(630,1050),1.0,10)

def backToHome():
    print "Back to home screen..."
    for x in range (1,2):
        device.press('KEYCODE_BACK', 'DOWN_AND_UP')
        
    sleep(SHORT_TIME)    
    #device.press('KEYCODE_HOME', 'DOWN_AND_UP')
    #sleep(SHORT_TIME)

def clickButton(buttonID):
    # Click taking picture button;
    easy_device.touch(By.id(buttonID), MonkeyDevice.DOWN_AND_UP)

#
# Clear current logcat information
#
def clearLogcatInfo():
    cmd = "adb logcat -c"
    os.system(cmd) 

#
# Dump current logcat information
#
def getFullLogcatInfo():
    cmd = "adb logcat -d"
    aLog = os.popen(cmd).readlines()
    return aLog
    
#
# Get useful logcat information from dump logcat
#
def getUsefulLogcatInfo(sFind):
    aLog = getFullLogcatInfo()
    aFindLog = []
    for value in aLog:
        if sFind in value:
            aFindLog.append(value)
    return aFindLog
    
#
# Save DUT screenshot into results folder
#
def savePNGResult(name):
    sResult = sProjectPath + 'results/' + name + "(" + getSysTime() + ").png"
    result = device.takeSnapshot()
    print "Save result: %s" %(sResult)
    result.writeToFile(sResult ,'png')
    
#
# Save strings into results folder
#
def saveTXTResult(name,sFileContent):
    sResult = sProjectPath + 'results/' + name + "(" + getSysTime() + ").txt"
    print " Save result: %s" %(sResult)    
    f=open(sResult, 'w')
    f.writelines(sFileContent)
    f.close()

#
# Get current system time and format it for file name.
#
def getSysTime():
    return time.strftime("%Y-%m-%d_%H-%M",time.localtime(time.time()))

# ---------- END: Common functions ---------- #


def main():

	print "------  CaseID = %s, Looptimes = %d ------" %(CaseID, iLOOPTIMES)

	global device  
	global easy_device

	device = getDevice()
    #easy_device = getEasyDevice()
    
    # Start testing
	print 'Test start here:'
	
#	setUp()

#	launchCamera()
	for i in range (0,iLOOPTIMES):
		print '->Loop time: %4d' %(i+1)
		processTestCase(i)
    
    # End...
	print "------  CaseID = %s, END ------" %(CaseID)
    
if __name__ == '__main__':
    main()
