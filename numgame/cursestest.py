# this is from youtube channel 'tech with tim' -- 5 part series

# from cmath import rect
import curses
from curses import wrapper, can_change_color
from curses.textpad import Textbox, rectangle
import time

def main(stdscr):

    # initialize a color pair: (id, fg color, bg color)
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    YELBLU = curses.color_pair(1)
    REDWHT = curses.color_pair(2)

    stdscr.clear()
    stdscr.addstr(2,5,"underline -- Stormy Forrest fuzzy moose squiki...", curses.A_UNDERLINE)
    stdscr.addstr(3,5,"bold -- Stormy Forrest fuzzy moose squiki...", curses.A_BOLD)
    stdscr.addstr(4,5,"color -- Stormy Forrest fuzzy moose squiki...", YELBLU)
    stdscr.addstr(5,5,"color -- Stormy Forrest fuzzy moose squiki...", REDWHT)
    stdscr.addstr(6,5,"change color: " + str(can_change_color()))
    rows, cols = stdscr.getmaxyx()
    stdscr.addstr(7,5,"console size ([rows][cols]): [" + str(rows) + '][' + str(cols) + ']')
    
    # stdscr.getch()

    # create a window... (height, length, row, col)
    counter_win = curses.newwin(1,20,10,5)


    # updating the screen:
    for i in range(10):
        color = YELBLU

        if i % 2 == 0:
            color = REDWHT
        
        # clear the std out:
        # stdscr.clear()

        # clear the 'window' created above:
        counter_win.clear()

        # use std out:
        # stdscr.addstr(2,5, f"Num:  {i}", color)
        # stdscr.refresh()

        # use the window created above
        counter_win.addstr(f"Num:  {i}", color)
        counter_win.refresh()

        time.sleep(0.2)


    # get some user input...
    stdscr.addstr(12,5,"Type something: ")
    key = stdscr.getkey()
    stdscr.addstr(13,5,f"You typed: {key}")
    stdscr.getch()

    # get the arrow key input...
    y,x = 15,5
    stdscr.addstr(14,5,"Press the arrow keys (q to quit)...")

    # make the loop non-blocking: 
    stdscr.nodelay(True)
    while True:
        # need try block for non-blocking:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key == "KEY_LEFT":
            x -= 1
        if key == "KEY_RIGHT":
            x += 1
        if key == "KEY_UP":
            y -= 1
        if key == "KEY_DOWN":
            y += 1 
        if key == "q":
            break
        
        # stdscr.clear()
        stdscr.addstr(y, x, ".")
        stdscr.refresh()

    # turn on blocking 
    stdscr.nodelay(False)

    # draw a rectangle:
    rectangle(stdscr, 20,5,30,25) # winobj, uly,ulx,lry,lrx)
    stdscr.refresh()
    stdscr.getch()



wrapper(main)


