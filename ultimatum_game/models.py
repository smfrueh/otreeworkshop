from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum_game'
    players_per_group = 2
    num_rounds = 1
    endowment = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    ug_decision = models.CurrencyField (min=0,
                                      max=Constants.endowment,
                                      verbose_name= 'How much money are you willing to send?',
                                      doc="dictator's decision")
    ug_accept = models.BooleanField()

    def set_payoffs(self):
        dictator = self.get_player_by_role('dictator')
        receiver = self.get_player_by_role('receiver')
       # if ug_accept == 'True':
        #    dictator.payoff = Constants.endowment - self.ug_decision
         #   receiver.payoff = self.ug_decision,
        #else:
         #   dictator.payoff = 0
          #  receiver.payoff = 0




class Player(BasePlayer):

    def role(self):
        if self.id_in_group == 1:
            return 'dictator'
        else:
            return 'receiver'
