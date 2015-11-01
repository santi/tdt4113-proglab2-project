from operator import attrgetter

__author__ = 'estensen'


class Arbitrator:
    def __init__(self):
        pass

    def choose_action(self, active_behaviors):
        """Choose winning behavior.

        Returns
        -------
        motor_recommendation : On the format (action, duration).
        """
        winning_behavior = max(active_behaviors, key=attrgetter('weight'))
        print("Winning behavior is " + str(winning_behavior.motor_recommendation))
        return winning_behavior.motor_recommendation
