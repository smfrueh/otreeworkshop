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
    name_in_url = 'political_views'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.treatment = random.choice([True, False])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.BooleanField()
    choice = models.StringField(widget=widgets.RadioSelectHorizontal)
    selection = models.IntegerField(verbose_name="Choose your political position from 0 to 10, 0 being left",
                                    widget=widgets.Slider(attrs={'step': '1', }), min=0, max=10)
