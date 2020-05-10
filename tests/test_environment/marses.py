import data_objects as do

default_mars = do.Mars(do.Grid(5, 5), [
    do.RoverSetup(do.Rover(1, 2, 'N'), ['L', 'M', 'L', 'M', 'L', 'M', 'L', 'M', 'M']),
    do.RoverSetup(do.Rover(3, 3, 'E'), ['M', 'M', 'R', 'M', 'M', 'R', 'M', 'R', 'R', 'M'])
])
