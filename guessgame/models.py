from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Seraina Frueh'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'guessgame'
    players_per_group = None
    num_rounds = 1
    endowment = 100
    minguess = 0
    maxguess = 100



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    guess = models.IntegerField()
    toguess = models.IntegerField()
    def set_payoff(self):
        self.payoff = Constants.endowment - abs(self.toguess - self.guess)