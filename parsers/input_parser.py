from data_objects import Grid, Rover, RoverSetup, Mars


def parse(commands):
    x, y = commands[0].upper().split()
    grid = Grid(int(x), int(y))

    rover = None
    rover_setups = []
    for idx, command in enumerate(commands[1:]):
        if idx % 2 == 0:
            rover_x, rover_y, direction = command.upper().split()
            rover = Rover(int(rover_x), int(rover_y), direction)
        else:
            rover_setups.append(RoverSetup(rover, [char for char in command.upper()]))

    return Mars(grid, rover_setups)
