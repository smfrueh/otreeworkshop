from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass


class Decision1(Page):
    form_model = 'player'
    form_fields = ['choice']

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
                'image2': image2,}



class Results(Page):
    pass


page_sequence = [
    Intro,
    Decision1,
    Results
]
