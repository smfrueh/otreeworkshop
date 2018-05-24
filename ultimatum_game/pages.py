from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    def vars_for_template(self):
        animals = ['cat', 'dog', 'mouse', 'rat']
        return {'animals': animals}

class Control(Page):
    form_model = 'player'
    form_fields = ['control1']

    def control1_error_message(self, value):
        if value != 90:
            return 'Value incorrect'



class DecisionSend(Page):
    form_model = 'group'
    form_fields = ['ug_decision']

    def is_displayed(self):
        return self.player.role() == 'dictator'


class DecisionAccept(Page):
    form_model = 'group'
    form_fields = ['ug_accept']

    def is_displayed(self):
        return self.player.role() == 'receiver'


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results1(Page):
    pass


class Results(Page):
    pass


page_sequence = [
    Intro,
    Control,
    DecisionSend,
    WaitPage,
    DecisionAccept,
    ResultsWaitPage,
    Results,

]
