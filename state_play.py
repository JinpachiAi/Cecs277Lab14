from puppy_state import PuppyState


class StatePlay(PuppyState):
    def feed(self, puppy):
        """
        When the puppy is playing, it ignores food
        Args:
            puppy (object): targets object

        Returns:
            puppy reaction (str) : A string of how the puppy will react depending on its current state
        """
        return "The puppy is too busy playing with the ball to eat right now."

    def play(self, puppy):
        """
        When the puppy is playing, playing more will make it continue playing
        If played with too much (2-3 times), it falls asleep; changes state to asleep
        Args:
            puppy (object): target object

        Returns:
            puppy reaction (str) : A string of how the puppy will react depending on its current state
        """
        puppy.inc_plays()

        if puppy.plays >= 2:
            from state_asleep import StateAsleep
            puppy.change_state(StateAsleep())
            return "The puppy played so much it fell asleep!"
        else:
            return "You throw the ball again and the puppy excitedly chases it."