# // The "abstraction" defines the interface for the "control"
#     // part of the two class hierarchies. It maintains a reference
# // to an object of the "implementation" hierarchy and delegates
# // all of the real work to this object.
from __future__ import annotations
from abc import ABC, abstractmethod


class Device(ABC):

    def __init__(self):
        self.on = False
        self.channel = 0
        self.volume = 0

    def isEnabled(self):
        return self.on

    def enable(self):
        print(self.name, 'Power ON ')
        self.on = True

    def disable(self):
        print(self.name, 'power off ')
        self.on = False

    def getVolume(self):
        return self.volume

    def setVolume(self, percent):
        print(self.name, 'setVolume ', percent)
        self.volume = percent

    def getChannel(self):
        return self.channel

    def setChannel(self, channel):
        self.channel = channel


class RemoteControl():
    def __init__(self, device):
        self.device = device

    def togglePower(self):
        if self.device.isEnabled():
            self.device.disable()
        else:
            self.device.enable()

    def volumeDown(self):
        self.device.setVolume(self.device.getVolume() - 10)

    def volumeUp(self):
        self.device.setVolume(self.device.getVolume() + 10)

    def channelDown(self, ):
        self.device.setChannel(self.device.getChannel() - 1)

    def channelUp(self, ):
        self.device.setChannel(self.device.getChannel() + 1)


# // You can extend classes from the abstraction hierarchy
# // independently from device classes.
class AdvancedRemoteControl(RemoteControl):
    def mute(self, ):
        self.device.setVolume(0)


class TV(Device):
    def __init__(self):
        self.name = 'TV'
        super().__init__()


class Radio(Device):

    def __init__(self):
        self.name = 'Radio'
        super().__init__()


if __name__ == "__main__":
    tv = TV()
    remote = RemoteControl(tv)
    remote.togglePower()

    radio = Radio()
    remote = AdvancedRemoteControl(radio)
    remote.mute()
