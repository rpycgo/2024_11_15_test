from abc import ABC, abstractmethod

class InterestStrategy(ABC):
    @abstractmethod
    def apply_interest(self, money):
        pass
