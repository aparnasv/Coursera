# implementation of card game - Memory

import simplegui
import random
import time

num=range(0,8) + range(0,8)
random.shuffle(num)
cent=range(15,800,50)
exposed=[False] * 16;
click_pos=[];
clickflag=True
cardidx1=0;
cardidx=0;
Turn=0


# helper function to initialize globals
def new_game():
    global num
    global exposed
    global Turn
    random.shuffle(num)
    exposed=[False] * 16;
    label.set_text("Turns = 0");
    pass  

def getcard(p):     
    if(p[1]<28 or p[1]>72):
        return 17
    for i in range(len(cent)):
        if(p[0]>cent[i]-12 and p[0]<cent[i]+32):
            return i
    return 17    
    pass

def timer_handler():
    exposed[cardidx]=not exposed[cardidx]
    exposed[cardidx1]=not exposed[cardidx1]
    timer.stop()
    pass

timer = simplegui.create_timer(750, timer_handler)

# define event handlers
def mouseclick(pos):
    global clickflag
    global cardidx1
    global cardidx
    global Turn
    if not timer.is_running():
         cardidx=getcard(list(pos))
         if (cardidx <17):
            if not exposed[cardidx]: 
                if clickflag:
                    cardidx1=cardidx
                    exposed[cardidx]=not exposed[cardidx]
                else:
                    exposed[cardidx]=not exposed[cardidx]
                    if(num[cardidx]==num[cardidx1]):
                         print "correct"
                    else:
                         timer.start()
                         Turn +=1
                         label.set_text("Turn = " + str(Turn))
                clickflag = not clickflag
    pass
    

# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(cent)):
        if exposed[i]:
            canvas.draw_text(str(num[i]), [cent[i],60], 30, "Green")
        else:
            canvas.draw_polygon([(cent[i], 40), (cent[i]+20, 40), (cent[i]+20, 60), (cent[i], 60)], 24, 'Green')

    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
