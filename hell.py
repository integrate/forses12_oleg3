import wrap
from wrap import sprite
import mario, mario_costume, dragon_costume
import bloks


def add_heart(x, y):
    id=sprite.add('hell', x, y, 'сердце1')
    return id


hell = [add_heart(15, 15), add_heart(50, 15), add_heart(85, 15)]
