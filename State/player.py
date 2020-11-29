from __future__ import annotations
from abc import ABC, abstractmethod

"""
The AudioPlayer class acts as a context. It also maintains a
reference to an instance of one of the state classes that
represents the current state of the audio player.
"""


class AudioPlayer(object):

    def __init__(self):
        self.state = ReadyState(self)
        self.playing = False

    # Other objects must be able to switch the audio player's active state.
    def change_state(self, state: State):
        print('Player changed to %s' % state)
        self.state = state
        self.playing = isinstance(state, PlayingState)

    # UI methods delegate execution to the active state.
    def click_clock(self, ):
        self.state.click_clock()

    def click_play(self):
        self.state.click_play()

    def click_next(self):
        self.state.click_next()

    def click_previous(self):
        self.state.click_previous()

    def play_next(self):
        print('Player play next song')

    def play_previous(self):
        print('Player play previous song')

    def fast_forward(self, time):
        print('Player forward %d s', time)

    def rewind(self, time):
        print('Player rewind %d s', time)


class State(ABC):
    """
    The base state class declares methods that all concrete states should implement and also provides a backreference to
    the context object associated with the state. States can use
    the backreference to transition the context to another state.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def click_clock(self, ):
        pass

    @abstractmethod
    def click_play(self, ):
        pass

    @abstractmethod
    def click_next(self, ):
        pass

    @abstractmethod
    def click_previous(self, ):
        pass


# Concrete states implement various behaviors associated with a state of the context.
class LockedState(State):

    # When you unlock a locked player, it may assume one of two states.
    def click_clock(self):
        if self.player.playing:
            self.player.change_state(PlayingState(self.player))
        else:
            self.player.change_state(ReadyState(self.player))

    def click_play(self, ):
        pass

    def click_next(self, ):
        pass

    def click_previous(self, ):
        pass


class ReadyState(State):
    def click_clock(self):
        self.player.change_state(LockedState(self.player))

    def click_play(self, ):
        self.player.startPlayback()
        self.player.change_state(PlayingState(self.player))

    def click_next(self, ):
        self.player.play_next()

    def click_previous(self, ):
        self.player.play_previous()


class PlayingState(State):
    def click_clock(self):
        self.player.change_state(LockedState(self.player))

    def click_play(self, ):
        self.player.stopPlayback()
        self.player.change_state(ReadyState(self.player))

    def click_next(self, event=None):
        if event == 'doubleclick':
            self.player.play_next()
        else:
            self.player.fast_forward(5)

    def click_previous(self, event=None):
        if event == 'doubleclick':
            self.player.play_previous()
        else:
            self.player.rewind(5)


if __name__ == '__main__':
    player = AudioPlayer()
    player.click_clock()
    player.click_next()

    player.click_clock()
    player.click_next()
    player.click_previous()