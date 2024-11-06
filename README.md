The original script defines poker hand ranges for 6-max play. It automatically
updates your position as you enter hands. It prints "True" if the hand is in the
defined raising range for the position and "False" if the hand is in the folding range
for the position. It also specifies calling and raising ranges for the big blind.

I then adapted that script into a GUI version using Tkinter. The GUI is easier to use.
It also includes a "Next" button to advance your position independently of entering hand
and raiser information and a "Clear" button to clear hand and raiser information. 
Note that for both versions, you must enter the higher card first (e.g. '98' not '89').