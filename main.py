from sensors import Sensors
from serial import Serial
from command import Plattform
import search_port
from sys import exit
import SendKeys

class Main():
    def __init__(self):
        self.filename = "config.txt"
        with open(self.filename) as f:
            config = f.read()
        self.config_list = [y for y in (x.strip() for x in config.splitlines()) if y]
        if self.find("onetouch") == "True":
            self.onetouch = True
        else:
            self.onetouch = False

        self.mysens = Sensors()
        self.mouse = Plattform()
        self.recived_data = None
        self.count = [0, 0, 0, 0,0]
        self.controlboard = []
        self.oldtouch = [False, False,False, False,False]
        self.touch = [False, False,False, False,False]
        self.sensibility = 0
        self.actived = True

        self.oldx = None
        self.oldy = None
        self.AS = [None,None,None] #X,Y,Z
        self.AA = [None, None, None]  # X,Y,Z
        self.GS = [None, None, None]  # X,Y,Z
        self.GA = [None, None, None]  # X,Y,Z

        self.mysens.setGyroscopeAngolData(X = 0.0, Y = 0.0, Z =  0.0)
        self.mysens.setGyroscopeScalledData(X=0.0, Y=0.0, Z=0.0)


    def find(self, keyword):
        return [s for s in self.config_list if keyword in s][0].split(" ")[1]

    def controlGyroscope(self):
        data = self.mysens.getGyroscopeScalledData()
        data2 = self.mysens.getGyroscopeAngolData()
        #print(data)

        if "SG" in self.recived_data:
            if self.recived_data[2] == "X":
                data[0] = float(self.recived_data.split(" ")[1])
            if self.recived_data[2] == "Y":
                data[1] = float(self.recived_data.split(" ")[1])
            if self.recived_data[2] == "Z":
                data[2] = float(self.recived_data.split(" ")[1])

        if "AG" in self.recived_data:
            if self.recived_data[2] == "X":
                data2[0] = float(self.recived_data.split(" ")[1])
            if self.recived_data[2] == "Y":
                data2[1] = float(self.recived_data.split(" ")[1])
            if self.recived_data[2] == "Z":
                data2[2] = float(self.recived_data.split(" ")[1])

        self.mysens.setGyroscopeScalledData(X = data[0], Y = data[1], Z = data[2])
        self.mysens.setGyroscopeAngolData(X=data2[0], Y=data2[1], Z=data2[2])

    def controlAccelerometer(self):
        #accelerometer data
        data = self.mysens.getAccelerometerScalledData()
        data2 = self.mysens.getAccelerometerScalledData()

        if "SA" in self.recived_data:
            if self.recived_data[2] == "X":
                data[0] = float(self.recived_data.split(" ")[1])
            if self.recived_data[2] == "Y":
                data[1] = float(self.recived_data.split(" ")[1])
            if self.recived_data[2] == "Z":
                data[2] = float(self.recived_data.split(" ")[1])

        if "AA" in self.recived_data:
            if self.recived_data[2] == "X":
                data2[0] = float(self.recived_data.split(" ")[1])
            if self.recived_data[2] == "Y":
                data2[1] = float(self.recived_data.split(" ")[1])
            if self.recived_data[2] == "Z":
                data2[2] = float(self.recived_data.split(" ")[1])

        self.mysens.setAccelerometerScalledData(X=data[0], Y=data[1], Z=data[2])
        self.mysens.setAccelerometerAngolData(X=data2[0], Y=data2[1], Z=data2[2])

    def controlOtherSensor(self):
        if self.recived_data.split(" ")[0] == "Temperature:": self.mysens.setTemperature(self.recived_data.split(" ")[1])

        #touch sensor data
        first = self.mysens.getTouchSensorFromIndex(0)
        second = self.mysens.getTouchSensorFromIndex(1)
        third = self.mysens.getTouchSensorFromIndex(2)
        fourth = self.mysens.getTouchSensorFromIndex(3)
        fifth = self.mysens.getTouchSensorFromIndex(4)

        if self.recived_data.split(" ")[0] == "Sensor1:":
            if int(self.recived_data.split(" ")[1]) == 1:
                first = True
            if int(self.recived_data.split(" ")[1]) == 0:
                first = False

        if self.recived_data.split(" ")[0] == "Sensor2:":
            if int(self.recived_data.split(" ")[1]) == 1:
                second = True
            if int(self.recived_data.split(" ")[1]) == 0:
                second = False

        if self.recived_data.split(" ")[0] == "Sensor3:":
            if int(self.recived_data.split(" ")[1]) == 1:
                third = True
            if int(self.recived_data.split(" ")[1]) == 0:
                third = False

        if self.recived_data.split(" ")[0] == "Sensor4:":
            if int(self.recived_data.split(" ")[1]) == 1:
                fourth = True
            if int(self.recived_data.split(" ")[1]) == 0:
                fourth = False

        if self.recived_data.split(" ")[0] == "Sensor5:":
            if int(self.recived_data.split(" ")[1]) == 1:
                fifth = True
            if int(self.recived_data.split(" ")[1]) == 0:
                fifth = False

        self.mysens.setTouchSensor(FIRST_SENSOR=first, SECOND_SENSOR=second,
                                   THIRD_SENSOR=third,FOURTH_SENSOR= fourth, FIFTH_SENSOR=fifth)

    def setRecivedData(self, data):
        self.recived_data = data

    def controlTouch(self):
        self.touch = self.mysens.getTouchSensors()

        if self.touch[0] == self.oldtouch[0]:
            pass
        else:
            self.oldtouch[0] = self.touch[0]
            if self.count[0] == 1:
                self.count[0] = 0

            elif self.count[0] == 0:
                self.count[0] = 1
                print("Sensor 1 pressed")
                self.pressKey(self.find("p1"))

        if self.touch[1] == self.oldtouch[1]:
            pass
        else:
            self.oldtouch[1] = self.touch[1]
            if self.count[1] == 1:
                self.count[1] = 0

            elif self.count[1] == 0:
                self.count[1] = 1
                print("Sensor 2 pressed")
                self.pressKey(self.find("p2"))

        if self.touch[2] == self.oldtouch[2]:
            pass
        else:
            self.oldtouch[2] = self.touch[2]
            if self.count[2] == 1:
                self.count[2] = 0

            elif self.count[2] == 0:
                self.count[2] = 1
                print("Sensor 3 pressed")
                self.pressKey(self.find("p3"))

        if self.touch[3] == self.oldtouch[3]:
            pass
        else:
            self.oldtouch[3] = self.touch[3]
            if self.count[3] == 1:
                self.count[3] = 0
                print("Sensor 4 pressed")
                self.pressKey(self.find("p4"))

            elif self.count[3] == 0:
                self.count[3] = 1

        if self.touch[4] == self.oldtouch[4]:
            pass
        else:
            self.oldtouch[4] = self.touch[4]
            if self.count[4] == 1:
                self.count[4] = 0

            elif self.count[4] == 0:
                self.count[4] = 1
                print("Sensor 5 pressed")
                self.pressKey(self.find("p5"))

    def setSensibility(self, sens):
        self.sensibility = sens

    def moveMouseFromGlove(self):
        #here i trasform gyroscope data in angles
        pass
        # if angles are > i move mouse in one direction, else, in the other direction
        data = self.mysens.getGyroscopeScalledData()
        x = int(data[2]*self.sensibility) #for the gyroscope this is the z
        y = int(data[0]*self.sensibility) #for the gyroscope this is the x

        x1,y1 = self.mouse.getCursor()
        self.mouse.moveCursor(x + x1, y + y1)

    def moveMouseFromBand(self):
        # here i trasform gyroscope data in angles
        pass
        # if angles are > i move mouse in one direction, else, in the other direction
        data = self.mysens.getGyroscopeScalledData()
        print(data)
        x = int(data[0] * self.sensibility)  # for the gyroscope this is the z
        y = int(data[1] * self.sensibility)  # for the gyroscope this is the x

        x1, y1 = self.mouse.getCursor()
        self.mouse.moveCursor(x + x1, y + y1)

    def pressKey(self,key):
        if key == "Active":
            if self.actived == True:
               self.actived = False
            elif self.actived == False:
                self.actived = True
        elif key == "False":
            pass
        else:
            try:
                SendKeys.SendKeys(key)
            except:
                print("Key doesn't recognized")


    def getActived(self):
        return self.actived

master = Main()
loop = True
if master.find("autoport"):
    try:
        port = search_port.serial_ports()[0]
    except IndexError:
        print("Arduino not recognized")
        exit(1)
    else:
        print("Autoport activated")
else:
    port = master.find("port")

arduino = Serial(port, int(master.find("baud")))
print("Connection start")
master.setSensibility(0.5)
while(loop):
    try:
        signal = arduino.readline()
    except:
        print("Unable to read data from Arduino")
        exit(1)
    master.setRecivedData(signal)
    master.controlGyroscope()
    master.controlOtherSensor()
    master.controlTouch()

    if master.getActived():
        master.moveMouseFromBand()
