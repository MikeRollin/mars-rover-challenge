

class Rover():
    #Initialize rover at location with bearing
    def __init__(self, bearing = 'N', x = 0, y = 0):
        self.bearing = bearing;
        self.x = x;
        self.y = y;
        
    #Update rover location on grid
    def updateLocation(self, x = 0 , y = 0): 
        self.x = x;
        self.y = y;
        
    #Update rover bearing
    def updateBearing(self, bearing = 'N'):
        self.bearing = bearing
    
    #Print rover location
    def printLocation(self):
        print str(self.x) + ' ' + str(self.y) + ' ' + self.bearing;