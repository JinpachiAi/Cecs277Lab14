from puppy_state import PuppyState
from state_eat import StateEat


class StateAsleep(PuppyState):
    def feed(self, puppy):
        """
        When the puppy is asleep and fed, it wakes up and comes running to eat
        changes state to Eating
        """
        puppy.reset()
        puppy.change_state(StateEat())
        return "The puppy wakes up and comes running to eat."

    def play(self, puppy):
        """
        When the puppy is asleep, you cannot play with it
        """
        return "The puppy is asleep. It doesn't want to play right now."