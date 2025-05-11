#Nana yang buat

import sys
from time import sleep

def print_lyrics():
    lines = [
        ("Oh, why can't we for once", 0.09),
        ("Say what we want", 0.1),
        ("Say what we feel?", 0.1),
        ("Oh, why can't you for once", 0.15),
        ("Disregard the world, and run", 0.09),
        ("To what you know is real?", 0.06),
        ("Take a chance with me", 0.09),
        ("Take a chance with me", 0.07)
    ]

    delays = [1, 0.9, 1.8, 0.3, 0.2, 0.6, 0.7, 0.3]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delays[i])
        print('')

print_lyrics()

