# Typing Test (Terminal Based)
A terminal-based typing speed test built using Python and the curses library. This program measures the user's typing speed (WPM) in real-time and provides different difficulty levels and modes.

## Features
- Real-time typing speed (WPM) calculation
- Two modes:
  - No Time Limit
  - 60-Second Timer
- Three difficulty levels:
  - Easy
  - Medium
  - Hard
- Loads random text based on selected difficulty
- Highlights:
  - Correct characters in green
  - Incorrect characters in red
- Backspace support for corrections
- Instant feedback while typing
- Fully interactive terminal UI using curses

## How the Program Works
- The program starts with a welcome screen.
- The user selects:
  - Mode (No time / 60 seconds)
  - Difficulty level (Easy, Medium, Hard)
- A random sentence is loaded from a file based on difficulty.
- The user starts typing:
  - WPM (Words Per Minute) is calculated in real-time.
  - Correct and incorrect characters are highlighted.
- The test ends when:
  - The user completes the sentence, OR
  - Time runs out (in 60-second mode)
- The user can restart or exit the program.

## How to Run the Program
1. Make sure **Python** is installed.
2. Run the program:
```bash
python main.py
```
> Note: This program uses the curses library, which works best on Linux/Mac terminals.  
> For Windows, you need to install:
```bash
pip install windows-curses
```

## File Structure
```bash
project/
│── main.py
│── Easy.txt
│── Medium.txt
│── Hard.txt
│── README.md
```

## Technologies Used
- Python
- curses (for terminal UI)
- time (for tracking typing speed)
- random (for selecting text)

## Notes
- Each difficulty file (Easy.txt, Medium.txt, Hard.txt) should contain multiple lines of text.
- The program randomly selects one line for each test.
- WPM is calculated using the standard formula:
  (characters typed / 5) / time in minutes
- Press ESC anytime to exit.

## Author
Muhammad Awais Tariq

If you like this project, consider giving it a star on GitHub!