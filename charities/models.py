import random
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'charities'
    players_per_group = None
    num_rounds = 1
    randlower = 1
    randupper = 100


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.charityA = random.choice([True, False])
            p.charityB = random.choice([True, False])
        for p in self.get_players():
            p.endowment = random.randint(Constants.randlower, Constants.randupper)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    endowment = models.IntegerField()
    charityA = models.BooleanField()
    charityB = models.BooleanField()
    choice = models.IntegerField(choices=((0, 'Hunger Coalition'),
                                          (1, 'Organ Donation')), verbose_name='Charities',
                                 widget=widgets.RadioSelectHorizontal)
