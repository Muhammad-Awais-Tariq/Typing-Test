import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\n Select mode 1.No time 2.60 seconds")
    stdscr.refresh()
    while True:
        try:
            mode = int(stdscr.getkey())
        except ValueError:
            stdscr.addstr("\nPlease enter a number")
            continue 
        if int(mode) not in [1,2]:
            stdscr.clear()
            stdscr.addstr("Invalid input. Please enter 1 or 2")
            stdscr.refresh()
        else:
            break
        
    stdscr.refresh()
    stdscr.addstr("\nSelect the level to start (1.Easy, 2.Medium, 3.Hard)")
    stdscr.refresh()
    while True:
        try:
            difficulty = int(stdscr.getkey())
        except ValueError:
            stdscr.addstr("\nPlease enter a number")
            continue 
        if int(difficulty) not in [1,2,3]:
            stdscr.clear()
            stdscr.addstr("Invalid input. Please enter 1, 2, or 3")
            stdscr.refresh()
        else:
            break
    
    return mode, difficulty
		

def display_text(stdscr, target, current, wpm=0):
	stdscr.addstr(target)
	stdscr.addstr(1, 0, f"WPM: {wpm}")

	for i, char in enumerate(current):
		correct_char = target[i]
		color = curses.color_pair(1)
		if char != correct_char:
			color = curses.color_pair(2)

		stdscr.addstr(0, i, char, color)

def load_text(difficulty):
	if difficulty == 1:
		with open("Easy.txt", "r") as f:
			lines = f.readlines()
			return random.choice(lines).strip()
	elif difficulty == 2:
		with open("Medium.txt", "r") as f:
			lines = f.readlines()
			return random.choice(lines).strip()		
	else:
		with open("Hard.txt", "r") as f:
			lines = f.readlines()
			return random.choice(lines).strip()		
			
def wpm_test(stdscr , difficulty , mode):
	universal_start_time = time.time()
	target_text = load_text(difficulty)
	current_text = []
	wpm = 0
	start_time = time.time()
	stdscr.nodelay(True)
	while True:
		time_elapsed = max(time.time() - start_time, 1)
		wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
		stdscr.clear()
		display_text(stdscr, target_text, current_text, wpm)
		stdscr.refresh()
		if mode == 2 and round(time.time()- universal_start_time) >= 60:
			break
		if "".join(current_text) == target_text:
			stdscr.nodelay(False)
			break
		if len("".join(current_text)) == len(target_text):
			stdscr.nodelay(False)
			break		
		try:
			key = stdscr.getkey()
		except:
			continue
		if ord(key) == 27:
			break
		if key in ("KEY_BACKSPACE", '\b', "\x7f"):
			if len(current_text) > 0:
				current_text.pop()
		elif len(current_text) < len(target_text):
			current_text.append(key)
def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
	
	while True:
		mode , difficulty = start_screen(stdscr)
		wpm_test(stdscr , difficulty ,mode)
		stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
		key = stdscr.getkey()
		
		if ord(key) == 27:
			break

wrapper(main)