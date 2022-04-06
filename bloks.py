import wrap
import time

time1=time.time()

def add_blok():
    blok=wrap.sprite.add('mario-items', 500, 500, 'block_bricks')
    return blok

def baka():
    global time1
    time2=time.time()
    if time2-time1>=5:
        a=add_blok()
        time1=time.time()
        return a



