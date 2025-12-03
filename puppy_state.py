from abc import ABC, abstractmethod


class PuppyState(ABC):
    """Interface for all puppy states"""

    @abstractmethod
    def feed(self, puppy):
        """Abstract method for feeding the puppy"""
        pass

    @abstractmethod
    def play(self, puppy):
        """Abstract method for playing with the puppy"""
        pass