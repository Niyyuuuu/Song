import sys
from time import sleep

def print_lyrics():

    lines = [
        # ("Temanku semua pada jahat", 0.07),
        # ("Tante", 0.12),
        # ("Aku lagi susah mereka ga ada", 0.08),
        # ("Coba kalau lagi jaya", 0.14),
        # ("Aku dipuja pujanya", 0.08),
        # ("Tante", 0.12),
        ("Sudah terbiasa terjadi", 0.08),
        ("Tante..", 0.12),
        ("Teman datang ketika lagi butuh saja", 0.09),
        ("Coba kalau lagi susah", 0.14),
        ("Mereka semua menghilang...", 0.08),
        ("Tante..", 0.12),
    ]

    # delays = [0.8, 1, 1.6, 0.4, 0.3, 1.5]
    delays = [0.6, 0.4, 0.3, 0.5, 3, 0.4]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delays[i])
        print('')

print_lyrics()

