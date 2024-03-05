from django.shortcuts import render, HttpResponse
from random import randint, choice
from django.views import View
import logging
from .forms import Game

LOGGER = logging.getLogger(__name__)


def log(func):
    def wrapper(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        # print(res.content)
        LOGGER.info(f'The function {func.__name__} was returned {response.content.decode()}')
        return response
    return wrapper


@log
def gen_coin(request, num):
    results = [choice(['орел', 'решка']) for _ in range(num)]
    context = {'game_name': "бросок монеты", 'results': results}
    return render(request, 'dice_app/game.html', context)


@log
def gen_dice(request, num):
    results = [randint(0, 7) for _ in range(num)]
    context = {'game_name': "бросок кости", 'results': results}
    return render(request, 'dice_app/game.html', context)


@log
def gen_rand_hundred(request, num):
    results = [randint(0, 100) for _ in range(num)]
    context = {'game_name': "случайное число от 0 до 100", 'results': results}
    return render(request, 'dice_app/game.html', context)


def game(request):
    if request.method == 'POST':
        form = Game(request.POST)
        if form.is_valid():
            choose = form.cleaned_data.get('choose')
            attempts = form.cleaned_data.get('attempts')
            if choose == 'coin':
                return gen_coin(request, attempts)
            if choose == 'dice':
                return gen_dice(request, attempts)
            if choose == 'rand_hundred':
                return gen_rand_hundred(request, attempts)
    else:
        form = Game()
    return render(request, 'dice_app/game1.html', {'form': form})
