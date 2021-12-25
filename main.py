import wrap
from wrap import sprite
import mario

wrap.world.create_world(1337,758,0,25)
wrap.world.set_back_image('mario.png')

mario_1=mario.add_mario(300,309)
mario_2=mario.add_mario(600,390)
mario.move_mario_y(mario_1)
