from unittest.mock import Mock
from services.move_commands import MoveCommandSelector, MoveToNorthCommand, MoveToEastCommand, \
    MoveToSouthCommand, MoveToWestCommand
from services.turn_commands import TurnCommandSelector, TurnLeftFromNorthCommand, TurnRightFromNorthCommand


def get_mocked_move_command_selector_north_command_only():
    mss = MoveCommandSelector()
    mss.select = Mock(name='get_command')
    mss.select.return_value = MoveToNorthCommand()
    return mss


def get_mocked_move_command_selector_east_command_only():
    mss = MoveCommandSelector()
    mss.select = Mock(name='get_command')
    mss.select.return_value = MoveToEastCommand()
    return mss


def get_mocked_move_command_selector_west_command_only():
    mss = MoveCommandSelector()
    mss.select = Mock(name='get_command')
    mss.select.return_value = MoveToWestCommand()
    return mss


def get_mocked_move_command_selector_south_command_only():
    mss = MoveCommandSelector()
    mss.select = Mock(name='get_command')
    mss.select.return_value = MoveToSouthCommand()
    return mss


def get_mocked_turn_command_selector_turn_left_from_north_command_only():
    tss = TurnCommandSelector()
    tss.select = Mock(name='get_command')
    tss.select.return_value = TurnLeftFromNorthCommand()
    return tss


def get_mocked_turn_command_selector_turn_right_from_north_command_only():
    tss = TurnCommandSelector()
    tss.select = Mock(name='get_command')
    tss.select.return_value = TurnRightFromNorthCommand()
    return tss
