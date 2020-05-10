from unittest.mock import Mock
from services.move_strategies import MoveStrategySelector, MoveToNorthStrategy, MoveToEastStrategy, \
    MoveToSouthStrategy, MoveToWestStrategy
from services.turn_strategies import TurnStrategySelector, TurnLeftFromNorthStrategy, TurnRightFromNorthStrategy


def get_mocked_move_strategy_selector_north_strategy_only():
    mss = MoveStrategySelector()
    mss.get_strategy = Mock(name='get_strategy')
    mss.get_strategy.return_value = MoveToNorthStrategy()
    return mss


def get_mocked_move_strategy_selector_east_strategy_only():
    mss = MoveStrategySelector()
    mss.get_strategy = Mock(name='get_strategy')
    mss.get_strategy.return_value = MoveToEastStrategy()
    return mss


def get_mocked_move_strategy_selector_west_strategy_only():
    mss = MoveStrategySelector()
    mss.get_strategy = Mock(name='get_strategy')
    mss.get_strategy.return_value = MoveToWestStrategy()
    return mss


def get_mocked_move_strategy_selector_south_strategy_only():
    mss = MoveStrategySelector()
    mss.get_strategy = Mock(name='get_strategy')
    mss.get_strategy.return_value = MoveToSouthStrategy()
    return mss


def get_mocked_turn_strategy_selector_turn_left_from_north_strategy_only():
    tss = TurnStrategySelector()
    tss.get_strategy = Mock(name='get_strategy')
    tss.get_strategy.return_value = TurnLeftFromNorthStrategy()
    return tss


def get_mocked_turn_strategy_selector_turn_right_from_north_strategy_only():
    tss = TurnStrategySelector()
    tss.get_strategy = Mock(name='get_strategy')
    tss.get_strategy.return_value = TurnRightFromNorthStrategy()
    return tss
