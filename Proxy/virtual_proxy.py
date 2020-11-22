from abc import ABC, abstractmethod


class HEVSuitMedicalAid(ABC):
    @abstractmethod
    def administer_morphine(self) -> str:
        pass


class HEVSuit(HEVSuitMedicalAid):
    def administer_morphine(self) -> str:
        return "Morphine administered."


class HEVSuitHumanInterface(HEVSuitMedicalAid):
    _physicalSuit: HEVSuit = HEVSuit()

    def administer_morphine(self) -> str:
        return self._physicalSuit.administer_morphine()


if __name__ == "__main__":
    humanInterface = HEVSuitHumanInterface()
    print(humanInterface.administer_morphine())
