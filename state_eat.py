from puppy_state import PuppyState


class StateEat(PuppyState):
    def feed(self, puppy):
        """
        When the puppy is eating, feeding it more will make it continue eating
        If fed too much (2-3 times), it falls asleep; changes state to asleep
        Args:
            puppy (object): target object

        Returns:
            puppy reaction (str) : A string of how the puppy will react depending on its current state
        """
        puppy.inc_feeds()

        if puppy.feeds >= 2:
            from state_asleep import StateAsleep
            puppy.change_state(StateAsleep())
            return "The puppy ate so much it fell asleep!"
        else:
            return "The puppy continues to eat as you add another scoop of kibble to its bowl."

    def play(self, puppy):
        """
        When the puppy is eating, playing with it will distract it and make it play
        Args:
            puppy (object): target object

        Returns:
            puppy reaction (str) : A string of how the puppy will react depending on its current state
        """
        puppy.reset()
        from state_play import StatePlay
        puppy.change_state(StatePlay())
        return "The puppy looks up from its food and chases the ball you threw."