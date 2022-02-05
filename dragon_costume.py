import wrap
from wrap import sprite


def set_costum_jump(mario):
    sprite.set_costume(mario['id'], 'dragon_throw1')


def set_costum_stand(mario):
    sprite.set_costume(mario['id'], 'dragon_stand1')
