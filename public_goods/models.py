from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods'
    players_per_group = 3
    num_rounds = 2
    endowment = 100
    coefficient = 2
    path_to_instructions = 'public_goods/InstructionsBLOCK.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pg_group_contr = models.IntegerField()
    average_contrib = models.IntegerField()
    def set_payoffs(self):
        self.pg_group_contr = sum([p.pg_ind_contr for p in self.get_players()])
        self.average_contrib = self.pg_group_contr/Constants.players_per_group
        split_pg_group_contr = (self.pg_group_contr * Constants.coefficient) / Constants.players_per_group
        for p in self.get_players():
            p.payoff = Constants.endowment - p.pg_ind_contr + split_pg_group_contr


class Player(BasePlayer):
    pg_ind_contr = models.CurrencyField(min=0,
                                        max=Constants.endowment,
                                        verbose_name='How much do you want to contribute to the project?', )
