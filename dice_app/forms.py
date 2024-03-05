from django import forms


class Game(forms.Form):
    choose = forms.ChoiceField(choices=[('coin', 'Монетка'), ('dice', 'Кости'),('rand_hundred', 'Случайное число')])
    attempts = forms.IntegerField(min_value=1, max_value=64)