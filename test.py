
import grid


#5 5
#
#1 2 N
#
#LMLMLMLMM
#
#3 3 E
#
#MMRMMRMRRM

theGrid = grid.Grid(5,5);
validMoveOrientations = ['R','L','M','V'];

def handleInput(stringInput = ''):
    instructions = stringInput.split(' ');
    global theGrid;
    
    #potential setup of new grid
    if len(instructions) == 2:
        try:
            if(int(instructions[0])>0 and int(instructions[1])>0):
                theGrid = grid.Grid(int(instructions[0]),int(instructions[1]))
                print "Created new grid with dimensions " + instructions[0] +',' +instructions[1]
            else:
                print "Grid size must be bigger than 0,0"
            
        except ValueError:
            print "Not a valid input for creating a new Grid, please check your spacing and make sure valid integers are used";
    #potentialy adding a new rover
    elif len(instructions) == 3:
        try:
            #valid bearing
            if instructions[2].upper() in grid.bearings:
                theGrid.addRover(int(instructions[0]),int(instructions[1]),instructions[2].upper());
                print "Added rover to the grid at " + instructions[0] +','+ instructions[1] + ' ' + instructions[2].upper()
            else:
                print "Invalid bearing given";
        except ValueError:
            print "Invalid co-ordinates given, please make sure valid instegers are given";
    #potentially updating location and bearing of rover
    elif len(instructions) == 1:
        #checking if valid moves and direction are given before executing 
        for command in instructions[0]:
            if command.upper() not in validMoveOrientations:
                print "Instructions contain invalid commands, please check your input";
                return;
        #Checking if there is a rover to receive instructions
        if len(theGrid.rovers) == 0:
                print "There are no rovers on the grid, please add a rover";
        else:
            for command in instructions[0]:
                if command.upper() == 'R' or command.upper() == 'L':
                    #updating position of latest rover
                    theGrid.updateBearing(theGrid.rovers[len(theGrid.rovers)-1],command.upper());
                elif command.upper() == 'M':
                    theGrid.moveRover(theGrid.rovers[len(theGrid.rovers)-1]);
                elif command.upper() == 'V':
                    print "Printing out locations for rovers"
                    theGrid.printRoverPositions()
    else:
        print "Invalid instruction set, please check spacing and input"
        

if __name__=="__main__":
    #Test Input
    handleInput("5 5");
    handleInput("1 2 N")
    handleInput("LMLMLMLMM")
    handleInput("3 3 E")
    handleInput("MMRMMRMRRM")
    handleInput("V")
    print "-"*20
    print "Unit test complete"
    print "-"*20
    print "Create a new grid with: \"int int\""
    print "Add a rover to the grid with: \"int int bearing\""
    print "Add a list of commands for last rover: \"LRMV\" where 'R' = 90 degree right turn, 'L'= 90 degree left turn, 'M'= Move forward, 'V'= print locations of rovers on the grid curently"
    print "Use 'exit' to stop the application"    
    print "-"*20    
    print "Please input your own instructions:"
    instruction = raw_input('\n')
    while(instruction != 'exit'):
        handleInput(instruction)
        instruction = raw_input('\n')
        
    