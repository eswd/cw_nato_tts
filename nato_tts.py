#!/usr/bin/env python3
# nato_tts.py
# Reads input text using the NATO phonetic alphabet and espeak, with short pauses for spaces.

import sys
import subprocess
from time import sleep

NATO = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu',
    '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
    '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', ',': 'Comma',
    '=': 'Equal', '.': 'dot',
}

# Accept input from pipe, .txt file, command line, or prompt
if not sys.stdin.isatty():
    input_text = sys.stdin.read().strip()
elif len(sys.argv) > 1:
    # If the first argument ends with .txt, read from file
    if sys.argv[1].lower().endswith('.txt'):
        try:
            with open(sys.argv[1], 'r', encoding='utf-8') as f:
                lines = f.readlines()
            # If the first non-empty line is 'vvv[ka]', remove it
            idx = 0
            while idx < len(lines) and lines[idx].strip() == '':
                idx += 1
            if idx < len(lines) and lines[idx].strip().lower() == 'vvv[ka]':
                lines.pop(idx)
            # Füge an jedes Zeilenende ein Leerzeichen an
            input_text = ''.join(line.rstrip() + ' ' for line in lines).strip()
        except Exception as e:
            print(f"Error reading file {sys.argv[1]}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        input_text = ' '.join(sys.argv[1:])
else:
    input_text = input('Enter text: ')

# Build the NATO phrase list
nato_words = []
for char in input_text.upper():
    if char == ' ':
        # espeak: [[pau=300]] is a 300ms pause (silence)
        nato_words.append('<break time="1s"/>')
    elif char in NATO:
        nato_words.append(NATO[char])
    else:
        # For unknown chars, just say the char
        nato_words.append(char)

# Join into a single string
speak_text = ' '.join(nato_words)

# Call espeak
# Call espeak with -m to enable embedded commands (like [[pau=300]])
input("Press Enter to speak...")
sleep(1)
subprocess.run(['espeak-ng', '-s', '150', '-m', speak_text, '-g', '10', '-v', 'mb-en1'])
