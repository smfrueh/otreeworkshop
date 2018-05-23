from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
    pass


class Decision (Page):
    form_model = 'group'
    form_fields = ['dg_decision']

    def is_displayed(self):
        return self.player.role() == 'dictator'


class ResultsWaitPage(WaitPage):
    body_text = 'please wait for Dictator'

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    Intro,
    Decision,
    ResultsWaitPage,
    Results
]
