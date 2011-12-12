import curses, traceback

def main(stdscr):
  # Frame the interface area at fixed VT100 size
  global screen
  text = "This is a test"
  screen = stdscr.subwin(0, 0)
  screen.box()
  y, x = screen.getmaxyx()
  global cur_x, cur_y;
  cur_x = (x/2)-(len(text))/2
  cur_y = (y/2)
  screen.addstr( cur_y, cur_x, text) 
  
  screen.refresh()

  c = screen.getch()
  while c != ord('q'):
    screen.addstr(1,1,str(c))
    screen.refresh()
    if c == 65:
      move_up(text, screen) 
    elif c == 66:
      move_down(text, screen)
    elif c == 68:
      move_left(text, screen)
    elif c == 67:
      move_right(text, screen) 
    elif c == 410:
      y, x = screen.getmaxyx()
      #if curses.is_term_resized(y, x):
      screen.addstr(2,1, 'true')
      curses.resizeterm(y, x)
      move_center(text,screen)

    c = screen.getch()
  
  return

def move_up(text, screen):
  screen.clear()
  screen.box()
  global cur_y, cur_x
  cur_y = cur_y - 1
  screen.addstr( cur_y, cur_x, text)
  screen.refresh()
  
def move_down(text, screen):
  screen.clear()
  screen.box()
  global cur_y, cur_x
  cur_y = cur_y + 1
  screen.addstr( cur_y, cur_x, text)
  screen.refresh()
	
def move_right(text, screen):
  screen.clear()
  screen.box()
  global cur_y, cur_x
  cur_x = cur_x + 1
  screen.addstr( cur_y, cur_x, text)
  screen.refresh()

def move_left(text, screen):
  screen.clear()
  screen.box()
  global cur_y, cur_x
  cur_x = cur_x - 1
  screen.addstr( cur_y, cur_x, text)
  screen.refresh()

def move_center(text, screen):
  screen.clear()
  screen.box()
  global cur_y, cur_x
  y, x = screen.getmaxyx()
  cur_x = (x/2)-(len(text))/2
  cur_y = (y/2)
  screen.addstr( cur_y, cur_x, text)
  screen.refresh()

if __name__ == '__main__':
  try:
    # Initialize curses
    stdscr=curses.initscr()

    # Turn off echoing of keys, and enter cbreak mode,
    # where no buffering is performed on keyboard input
    curses.noecho()
    curses.cbreak()

    # In keypad mode, escape sequences for special keys
    # will be interpreted and a special value like
    # curses.KEY_LEFT will be returned
    stdscr.keypad(1)
    curses.curs_set(0)

    main(stdscr) # enter main loop
  except curses.error:
    # In the event of error, restore terminal to sane state
    traceback.print_exc() # Print the exception
    print(curses.ERR)
  except KeyboardInterrupt:
    # Caught KeyboardInterrupt (Gets rid of stacktrace)
    # Set everything back to normal
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
    exit()
  finally:
    # Set everything back to normal
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
