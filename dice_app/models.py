from django.db import models
from random import choice


class HeadsAndTailsModel(models.Model):
    SIDE = ('heads', 'tails')
    side = models.CharField(max_length=10, default=choice(SIDE))
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Монета упала стороной "{self.side}"'

    @staticmethod
    def det_info(num):
        info = HeadsAndTailsModel.object.all()[-num:]
        head_count = sum(i.side == 'head' for i in info)
        tail_count = num - head_count
        return {'head': head_count, 'tail': tail_count}