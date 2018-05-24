from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass


class Decision1(Page):
    form_model = 'player'
    form_fields = ['choice']

    def vars_for_template(self):
        if self.player.treatment:
            return {'image1': 'political_views/PdA.jpg',
                    'image2': 'political_views/SVP-UDC_rgb.jpg'}
        else:
            return {'image1': 'political_views/PCD_Logo_ro_RGB.jpg',
                    'image2': 'political_views/SP_Logo_cmyk.jpg'}

    def choice_choices(self):
        if self.player.treatment:
            return ['PdA', 'SVP']
        else:
            return ['SP', 'EVP']


class Decision2(Page):
    form_model = 'player'
    form_fields = ['selection']


class Results(Page):
    pass


page_sequence = [
    Intro,
    Decision1,
    Decision2,
    Results
]
