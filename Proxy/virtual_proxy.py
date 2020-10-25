from abc import ABC, abstractmethod
from tokenize import String
from traitlets import Bool

class HEVSuitMedicalAid(ABC):
    @abstractmethod
    def administerMorphine(self) -> String:
        pass


class HEVSuit(HEVSuitMedicalAid):
    def administerMorphine(self) -> String:
        return "Morphine administered."


class HEVSuitHumanInterface(HEVSuitMedicalAid):
    _physicalSuit: HEVSuit = HEVSuit()

    def administerMorphine(self) -> String:
        return self._physicalSuit.administerMorphine()


if __name__ == "__main__":
    humanInterface = HEVSuitHumanInterface()
    print(humanInterface.administerMorphine())
