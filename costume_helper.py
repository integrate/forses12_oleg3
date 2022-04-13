import wrap


def change_costume(id, costume):
    y = wrap.sprite.get_bottom(id)
    wrap.sprite.set_costume(id, costume)
    wrap.sprite.move_bottom_to(id, y)
