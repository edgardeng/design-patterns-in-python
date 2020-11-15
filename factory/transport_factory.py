from __future__ import annotations
from abc import ABC, abstractmethod


class TransportFactory(ABC):
    """
    The Creator class is supposed to return an object of a Product class.
    """

    @abstractmethod
    def create_transport(self):
        """
        Note that the Creator may also provide some default implementation of the factory method.
        """
        pass

    def plan_delivery(self) -> str:
        """
        some core business logic that relies on Product objects
        all transport object need to 'delivery'
        """

        # Call the factory method to create a Product object.
        transport = self.create_transport()
        result = f"Creator: The same creator's code has just worked with {transport.deliver()}"

        return result


class RoadTransport(TransportFactory):

    def create_transport(self):
        return Truck()


class SeaTransport(TransportFactory):

    def create_transport(self):
        return Ship()


class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass


class Truck(Transport):
    def deliver(self):
        return 'Truck: Delivery by land in a box'


class Ship(Transport):
    def deliver(self):
        return ' Ship: Delivery by sea in a container'


def client_code(creator: TransportFactory) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.plan_delivery()}")


if __name__ == "__main__":
    print("\r\nApp: Launched with the RoadTransport.\r\n")
    client_code(RoadTransport())

    print("\r\nApp: Launched with the SeaTransport.\r\n")
    client_code(SeaTransport())
