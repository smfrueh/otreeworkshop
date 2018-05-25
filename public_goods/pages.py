from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass


class Contribution(Page):
    form_model = 'player'
    form_fields = ['pg_ind_contr']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Results(Page):
    pass

class ResultsFINAL(Page):
    pass


page_sequence = [
    Intro,
    Contribution,
    ResultsWaitPage,
    Results,
    ResultsFINAL,
]
