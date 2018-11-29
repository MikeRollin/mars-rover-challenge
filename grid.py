
import rover

#Possible bearings for the rover        
bearings = ['N','E','S','W'];

class Grid():
    
    def __init__(self, x_boundary, y_boundary):
        self.x_boundary = x_boundary;
        self.y_boundary = y_boundary;
        self.rovers = [];
        
    def validMove(self, x, y):
        #Checking if location is off the grid
        if(x > self.x_boundary or x < 0 or y > self.y_boundary or y < 0):
            return False;
        #Checking if location is going to collide with another rover
        #Is no longer required, was a misunderstanding
#        for rover in self.rovers:
#            if (x == rover.x and y == rover.y):
#                return False;
        return True;
        
    def addRover(self, x, y, bearing):
        if self.validMove(x,y):
            self.rovers.append(rover.Rover(bearing, x, y))
        else:
            print "Invalid starting position for rover"
        
        
    def updateBearing(self, rover, right_left = 'R'):
        if right_left.upper() == 'R':
            #Add 90 degree (right turn), which directly relates to bearing array
            rover.updateBearing(bearing=bearings[(bearings.index(rover.bearing) + 1)%4])
        elif right_left.upper() == 'L':
            #Subtract 90 degree (left turn), which directly relates to bearing array
            #Added one full rotation to ensure that array does not go out of bounds
            rover.updateBearing(bearing=bearings[(bearings.index(rover.bearing) - 1 + 4)%4])
                  
    def moveRover(self, rover):
        #Move the rover according to the current bearing
        if rover.bearing == 'N':
            if self.validMove(rover.x, rover.y+1):
                rover.updateLocation(rover.x, rover.y+1);
            else:
                print "Out of bounds at " + str(rover.x) + ',' + str(rover.y+1)
        elif rover.bearing == 'E':
            if self.validMove(rover.x+1, rover.y):
                rover.updateLocation(rover.x+1, rover.y);
            else:
                print "Out of bounds at " + str(rover.x+1) + ',' + str(rover.y)
        elif rover.bearing == 'S':
            if self.validMove(rover.x, rover.y-1):
                rover.updateLocation(rover.x, rover.y-1);
            else:
                print "Out of bounds at " + str(rover.x) + ',' + str(rover.y-1)
        elif rover.bearing == 'W':
            if self.validMove(rover.x-1, rover.y):
                rover.updateLocation(rover.x-1, rover.y);
            else:
                print "Out of bounds at " + str(rover.x-1) + ',' + str(rover.y)
    
    def printRoverPositions(self):
        if len(self.rovers) == 0:
            print "There are no rovers on the grid currently, please add a rover"
        else:
            for _rover in self.rovers:
                _rover.printLocation()