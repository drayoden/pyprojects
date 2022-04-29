## Just messing around with some python between projects
- ### amazon pricer app
  ---
  * Origin: https://www.theinsaneapp.com/2021/06/list-of-python-projects-with-source-code-and-tutorials.html
  * amzpricer -- another crawler with email support
- ### work guess game -- like the one on my HP calculator
  - terminal game; using the python curses library
  - need a name: I can only think of the game 'wordle' which is very close but with numbers.
    - numdle, digdle,
  - requirements:
    - terminal game -- python curses
    - choose number of digits 3 to 10 -- default 3
    - subtracitve score -- start with x, each guess will subtract y? x is based on the number of digits chosen.
    - initial digit stream is random -- randomize each digit 0-9
    - use rectangles inside windows for multiple areas of play:
      - top: guess area -- present a list of guesses
      - guess box: place where user types a guess
      - bottom: status area: score, etc. 
    - each guess will display the list of the digits in the guess and use the foreground color to signify the status of each digit:
    - green: digit is in the stream and in the correct posistion
    - blue: digit is in the stream but not in the correct position
    - white: digit is not in the stream
  - psudocode:
```

```



