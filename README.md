# Typing-Test
A simple typing test made in python to find the typing speed of the user.

## Features
- Generates random arithmetic expressions
- Supports four operators: addition (+), subtraction (-), multiplication (*), and division (/)
- Allows the user to choose the number of questions
- Allows the user to define the maximum number range for generated problems
- Gives the user up to three attempts for each question
- Displays the correct answer if the user fails after three attempts
- Tracks and displays the final score
- Measures the total time taken to complete the quiz
- Simple command line interface for user interaction

## How the Program Works
Run the program and enter the required inputs when prompted.

- The program first asks the user how many questions they want to solve.
- Then it asks for the maximum number limit (for example: 10, 100, 1000). The generated numbers in the problems will stay within this range.
- The program generates random arithmetic expressions using two numbers and a random operator.
- The user attempts to solve each problem.
- The user has **three attempts** to answer each question correctly.
- If the user answers correctly, the score increases by 1.
- If the user fails all three attempts, the correct answer is displayed and the score decreases by 1.
- After all questions are completed, the program displays:
  - Total time spent solving the problems
  - Final score

## How to Run the Program
1. Make sure **Python** is installed.
2. Run the program:
```bash
python main.py
```

## File Structure
```bash
project/
│── main.py
│── README.md
```

## Technologies Used
- Python
- random
- time

## Notes
- The program runs in the terminal or command prompt.
- Division results are rounded before comparison with the user’s answer.
- The program uses Python's `eval()` function to calculate the correct answer for generated expressions.

## Author
Muhammad Awais Tariq

If you like this project, consider giving it a star on GitHub!