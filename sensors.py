class Sensors():
    def __init__(self):
        # A = angolo       S = scalato
        # G = gisoscopio   A = accelerometro   N = angolo
        # X = asse_x       Y = asse_y          Z = asse_z
        self.AA = [0.0, 0.0, 0.0]  # X,Y,Z
        self.SA = [0.0, 0.0, 0.0]  # X,Y,Z
        self.AG = [0.0, 0.0, 0.0]  # X,Y,Z
        self.SG = [0.0, 0.0, 0.0]  # X,Y,Z #this may be used for the glove
        self.AN = [0.0, 0.0, 0.0]  # X,Y,Z
        self.sensors = [False, False, False, False, False]



    def getAccelerometerScalledData(self):
        return self.SA

    def getAccelerometerAngolData(self):
        return self.AA

    def setAccelerometerScalledData(self, X=None, Y=None, Z=None):
        self.SA= [X, Y, Z]

    def setAccelerometerAngolData(self, X=None, Y=None, Z=None):
        self.AA = [X, Y, Z]



    def setAngolData(self,X=None, Y=None, Z=None):
        self.AN = [X, Y, Z]



    def getGyroscopeScalledData(self):
        return self.SG

    def getGyroscopeAngolData(self):
        return self.AG

    def setGyroscopeScalledData(self, X=0.0, Y=0.0, Z=0.0):
        self.SG = [X, Y, Z]

    def setGyroscopeAngolData(self, X=0.0 , Y=0.0 , Z=0.0):
        self.AG = [X,Y,Z]



    def getTouchSensorFromIndex(self, index):
        return self.sensors[index]

    def getTouchSensors(self):
        return self.sensors

    def setTouchSensor(self,FIRST_SENSOR = None, SECOND_SENSOR = None,
                       THIRD_SENSOR = None, FOURTH_SENSOR = None,
                       FIFTH_SENSOR = None):
        self.sensors[0] = FIRST_SENSOR
        self.sensors[1] = SECOND_SENSOR
        self.sensors[2] = THIRD_SENSOR
        self.sensors[3] = FOURTH_SENSOR
        self.sensors[4] = FIFTH_SENSOR
