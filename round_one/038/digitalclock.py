"""Digital Clock, by Obed Banda
Displays a digital clock of the current time with a seven-segment
display. Press Ctrl-C to stop.

Requires sevsg.py to be in the same folder.
Tags: tiny, artistic
"""

import sys, time
import sevseg

try:
    while True:  # Main program loop
        # Clear the secreen by printing several newlines:
        print('\n' * 60)

        # Get the current time from the computer's clock:
        currentTime = time.localtime()
        # % 12 so we can use a 12-hour clock, not 24:
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12'    # 12-hour clocks show 12:00, not 00:00
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        # Get the digits strings from sevseg module:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)

