from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Intro(Page):
    timeout_seconds = 5


class Decision1(Page):
    form_model = 'player'
    form_fields = ['donationA', 'donationB']
    timeout_seconds = 5

    def vars_for_template(self):
        if self.player.charityA:
            image1 = 'charities/im_persA.jpg'
        else:
            image1 = 'charities/im_genA.jpg'
        if self.player.charityB:
            image2 = 'charities/im_persB.jpg'
        else:
            image2 = 'charities/im_genB.jpg'
        return {'image1': image1,
                'image2': image2, }

    def donationA_max(self):
        return self.player.endowment

    def donationB_max(self):
        return self.player.endowment

    def error_message(self, values):
        if values["donationA"] + values["donationB"] < self.player.endowment:
            return 'You must donate your entire endowment.'
        if values["donationA"] + values["donationB"] > self.player.endowment:
            return 'You cannot donate more than your endowment.'

    def before_next_page(self):
        if self.timeout_happened:
            self.player.donationA = random.randint(1, self.player.endowment)
            self.player.donationB = self.player.endowment - self.player.donationA


class Results(Page):
    pass


page_sequence = [
    Intro,
    Decision1,
    Results
]
