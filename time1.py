import time
import wrap

a=time.time()




r=wrap.sprite.add_text('0',800,400 )
def time2():
    global c
    c=int(time.time()-a)
    print(c)


def text():
    wrap.sprite_text.set_text(r,str(c))

