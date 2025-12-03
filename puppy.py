from puppy_state import PuppyState
from state_asleep import StateAsleep


class Puppy:
    def __init__(self):
        """
        Initialize the puppy to the asleep state and set feeds/plays to 0
        """
        self._state = StateAsleep()
        self._feeds = 0
        self._plays = 0

    @property
    def feeds(self):
        """
        getter for feeds
        Returns:
            self._feeds : The amount of times the puppy has been fed in a row
        """
        return self._feeds

    @property
    def plays(self):
        """
        getter for plays
        Returns:
            self._plays : The amount of times the puppy has been played with in a row
                """
        return self._plays


    def change_state(self, new_state):
        """
        Updates the puppy's state to the new state
        """
        self._state = new_state

    def give_food(self):
        """
        Calls the feed method for whichever state the puppy is in
        """
        print(self._state.feed(self))

    def throw_ball(self):
        """
        Calls the play method for whichever state the puppy is in
        """
        print(self._state.play(self))

    def inc_feeds(self):
        """
        Increments the number of times the puppy has been fed in a row
        """
        self._feeds += 1

    def inc_plays(self):
        """
        Increments the number of times the puppy has been played with in a row
        """
        self._plays += 1

    def reset(self):
        """
        Resets the feeds and plays attributes to 0
        """
        self._feeds = 0
        self._plays = 0