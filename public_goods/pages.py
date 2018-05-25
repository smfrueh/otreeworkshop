from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1


class Contribution(Page):
    form_model = 'player'
    form_fields = ['pg_ind_contr']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        data = [g.average_contrib for g in self.group.in_all_rounds()]
        series = [{'name': 'Contribution', 'type': 'column', 'data': data}]
        return {'series': series}


class End(Page):
    def vars_for_template(self):
        image1 = 'public_goods/smiley2.jpg'
        return {'image1': image1}

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    Intro,
    Contribution,
    ResultsWaitPage,
    Results,
    End,
]
