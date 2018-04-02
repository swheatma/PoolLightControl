#!/usr/bin/env python

# import RPi.GPIO as GPIO
import time

# set variables
left = 11    #GPIO17
right = 12   #GPIO18

Spa = 15 #GPIO22
Pool = 16 #GPIO23


delay = 300     #door open limit in seconds (production version)
#delay = 5     #door open limit in seconds (debug version)

OPEN = "open"
CLOSED = "closed"

door_delay = 15  # Time is takes for the door to close (in seconds)

def GPIOsetup():
    GPIO.setmode(GPIO.BOARD) # use GPIO pinout references (not GPIO number)
    GPIO.setwarnings(False)
    GPIO.setup(left, GPIO.IN)
    GPIO.setup(right, GPIO.IN)
    GPIO.setup(R_Door, GPIO.OUT)
    GPIO.setup(L_Door, GPIO.OUT)

    GPIO.output(R_Door,False)
    GPIO.output(L_Door,False)

#check door status
def door_status(x1):
    return OPEN if GPIO.input(x1) else CLOSED

def SetColor(Unit,ColorCode):
    print (ColorCode)
    for i in range (0,ColorCode):
        print "Light On"
        #GPIO.output(door, True)
        time.sleep(1)
        print "Light Off\n",
        #GPIO.output(door,False)


def mainGarage():    
    while True:

        if door_status(right) == OPEN:
            RElapsed = time.time() - RClosed
            if RElapsed > delay:
                print "Right Door has been open ", RElapsed, " second"
                print "Right Door has been open too long, closing..."
                closeDoor(R_Door)

                for i in xrange(door_delay):
                    time.sleep(1)
                    print ".",
                print ""

                #time.sleep(door_delay)
                print "Door should now be closed"
            else:
                RElapsed = time.time() - RClosed
                print "Right Door has been open ", RElapsed, " second"
        else:
            print "Right Door is closed"
            RClosed = time.time()
        if door_status(left) == OPEN:
            LElapsed = time.time() - LClosed
            if LElapsed > delay:
                print "Left Door has been open ", LElapsed, " second"
                print "Left Door has been open too long, closing",
                closeDoor(L_Door)
                for i in xrange(door_delay):
                    time.sleep(1)
                    print ".",
                print ""
                #time.sleep(door_delay)
                
                print "Door should now be closed"
            else:
                LElapsed = time.time() - LClosed
                print "Left Door has been open ", LElapsed, " second"
        else:
            print "Left Door is closed"
            LClosed = time.time()
        time.sleep(1)


def main():    

    colors = {
        '1' : "Show-Voodoo Lounge",
        '2' : "Fixed-Deep Blue Sea",
        '3' : "Fixed-Royal Blue",
        '4' : "Fixed-Afternoon Skies",
        '5' : "Fixed-Aqua Green",
        '6' : "Fixed-Emerald",
        '7' : "Fixed-Cloud White",
        '8' : "Fixed-Warm Red",
        '9' : "Fixed-Flamingo",
        '10' : "Fixed-Vivid Violet",
        '11' : "Fixed-Sangria",
        '12' : "Show-Twilight",
        '13' : "Show-Tranquility",
        '14' : "Show-Gemstone",
        '15' : "Show-USA",
        '16' : "Show-Mardi Gras",
        '17' : "Show-Cool Cabaret"
	}

    print ("Available colors are:\n")
    for key, value in sorted(colors.items()):
        print key, value

    var = raw_input("\nWhat color do you want? ")
    print(colors[var])

    SetColor(Spa,int(var))
    
if __name__ == "__main__":
#    GPIOsetup()
    main()
    
