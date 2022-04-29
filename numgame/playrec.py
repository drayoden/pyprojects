# center window with rectangle in console...

import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time


WCOLS = 30
WROWS = 10

#statchar = chr(126) # tilde
statchar = chr(45) # hyphen/minus


def main(scr):

    # get console size:
    conrows, concols = scr.getmaxyx()

    # color pairs:
    curses.use_default_colors()  # allows us to use the default console colors
    curses.init_pair(1, curses.COLOR_YELLOW, -1) # -1 -> default bg color 
    YELBG = curses.color_pair(1)

    # turn off blocking:
    #scr.nodelay(True)

    # new window (centered in console):
    centr = int(conrows/2) - int(WROWS/2)
    centc = int(concols/2) - int(WCOLS/2)

    # position of status line bottom of window:
    statr = WROWS - 2  

    win = curses.newwin(WROWS,WCOLS,centr,centc)

    win.clear()
    win.addstr(1,1,f"console rows: {str(conrows)}\n")
    win.addstr(2,1,f"console cols: {str(concols)}")
    
    # show status:
    win.addstr(statr -1,1, statchar * (WCOLS - 2),YELBG)
    # win.hline(statr - 1,1,statchar,WCOLS -2)
    win.addstr(statr,1,f"STATUS: -------")
    
    
    win.border()
    win.refresh()

    win.getch()



    # turn on blocking 
    #scr.nodelay(False)

    #scr.getch()

wrapper(main)