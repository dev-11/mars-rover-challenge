import data_objects as do

default_mars = do.Mars(do.Grid(5, 5), [
    do.RoverSetup(do.Rover(1, 2, 'N'), ['L', 'M', 'L', 'M', 'L', 'M', 'L', 'M', 'M']),
    do.RoverSetup(do.Rover(3, 3, 'E'), ['M', 'M', 'R', 'M', 'M', 'R', 'M', 'R', 'R', 'M'])
])

small_mars_with_one_rover_empty_commands = do.Mars(do.Grid(1, 1), [
    do.RoverSetup(do.Rover(0, 0, 'N'), [])
])
