from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Routing(ABC):
    """
    routing algorithm can be extracted to its own class with a single buildRoute method.
    The method accepts an origin and destination and returns a collection of the route’s checkpoints.

    """
    @abstractmethod
    def build_route(self, start_point, end_point):
        pass


class BusRouting(Routing):
    def build_route(self, start_point, end_point):
        print('go to <%s> from <%s> by Bus' % (end_point, start_point))


class BikeRouting(Routing):
    def build_route(self, start_point, end_point):
        print('go to <%s> from <%s> by Bike' % (end_point, start_point))


class CabRouting(Routing):
    def build_route(self, start_point, end_point):
        print('go to <%s> from <%s> by cab' % (end_point, start_point))


class Transportation(object):
    def __init__(self, routing: Routing):
        self._route = routing

    @property
    def routing(self) -> Routing:
        return self._route

    @routing.setter
    def routing(self, routing: Routing):
        self._route = routing

    def navigate(self, start, end):
        self._route.build_route(start, end)


if __name__ == '__main__':
    to_airport = Transportation(BusRouting())
    to_airport.navigate('home', 'airport')
    to_airport.routing = BikeRouting()
    to_airport.navigate('home', 'airport')