from abc import ABC, abstractmethod
from tokenize import String
from traitlets import Bool


class DoorOpening(ABC):
    @abstractmethod
    def open(self, doors: String) -> String:
        pass


class HAL9000(DoorOpening):
    def open(self, doors: String) -> String:
        return ("HAL9000: Affirmative, Dave. I read you. Opened \(doors).")


class CurrentComputer(DoorOpening):
    _computer: HAL9000 = None

    def authenticate(self, password: String) -> Bool:
        if password == "pass":
            self._computer = HAL9000()
            return True
        else:
            return False

    def open(self, doors: String) -> String:
        if self._computer:
            return self._computer.open(doors)
        else:
            return "Access Denied. I'm afraid I can't do that."


if __name__ == "__main__":
    computer = CurrentComputer()
    podBay = "Pod Bay Doors"
    print(computer.open(podBay))

    computer.authenticate("pass")
    print(computer.open(podBay))
