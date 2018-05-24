from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass

class DecisionSend (Page):
    form_model = 'group'
    form_fields = ['ug_decision']

    def is_displayed(self):
        return self.player.role() == 'dictator'

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results1 (Page):
    pass

class DecisionAccept (Page):
    form_model = 'group'
    form_fields = ['ug_accept']
    def is_displayed(self):
        return self.player.role() == 'receiver'

class Results(Page):
    pass


page_sequence = [
    Intro,
    DecisionSend,
    WaitPage,
    DecisionAccept,
    ResultsWaitPage,
    Results,

]
