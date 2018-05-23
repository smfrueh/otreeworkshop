from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'dictator_game'
    players_per_group = 2
    num_rounds = 1
    endowment = 100
    dictator_role_name = "dictator"
    sender_role_name = "sender"

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    dg_decision = models.CurrencyField(min=0,
                                      max=Constants.endowment,
                                      verbose_name= 'How much money would you like to send?',
                                      doc="dictator's decision")
    def set_payoffs(self):
        dictator = self.get_player_by_role('dictator')              ###or dictator = self.get_player_by_id(1)
        receiver = self.get_player_by_role ('receiver')
        dictator.payoff = Constants.endowment - self.dg_decision
        receiver.payoff = self.dg_decision


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'dictator'
        else:
            return 'receiver'