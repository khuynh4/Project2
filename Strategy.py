import abc
import random  # to use it for Cat class, in RandomCatBehavior


class RandomBehavior(object):   # Random Behavior Interface
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def sleepRandomly(self):
        """Random"""


class RandomCatBehavior(RandomBehavior):  # Interface for Cat's random action, will be used for delegation

    def sleepRandomly(self):
        randomStuff = []
        # List of actions a cat might do if it was asked to sleep
        action1 = "the Cat is sleeping"
        action2 = "the Cat is mewoing"
        action3 = "the Cat is running around"

        randomStuff.append(action1)
        randomStuff.append(action2)
        randomStuff.append(action3)

        finalAction = str(random.choice(randomStuff))  # Choose a random action when we ask a cat to sleep
        # Convert finalAction to String by using str() so we can return it
        return finalAction
