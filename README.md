# cw_nato_tts

Ein Skript um sich am Terminal cw ausgeben zu lassen was anschließend per TTS vorgelesen wird. Basiert auf dem `cwkoch.lua` Skript von Hanno zum CW erzeugen, zu finden hier: `https://github.com/silizium/crypto`. Nutzt aktuell espeak für TTS. Klingt zwar recht mechanisch, funktioniert aber fürs Erste.

## Wie funktioniert es?

`cwkoch.lua` erzeugt nach entsprechenden Parametern die Morsegruppen. Welche Buchstaben/Zahlen etc., die Geschwindigkeit etc. werden hierüber erzeugt. Das Ganze wird an CW für die Ausgabe gegeben.

Das Python Skrip `nato_tts.py` sorgt nur dafür das die TTS-Engine auch ICAO-Alphabet bzw. NATO Alphabet ausgibt. Wir wollen im Afu ja nicht A,B,C sondern Alpha, Bravo, Charlie vorgelesen bekommen. Das Ganze leider über eine seperate Textdatei aber das bekommt der Anwender in der Regel nicht mit.

Hab ich nicht geschrieben, hab mit einer KI verhandelt und die hat das zusammen gebastelt.

## Setup

1. Ein bissl apt für Lua und espeak: `sudo apt install espeak-ng cw luajit lua-posix mbrola mbrola-en1`
2. `cwkoch.lua` von hier holen und zum Laufen bringen```https://github.com/silizium/crypto```.
3. Dafür sorgen das `nato_tts.py` und `cwkoch.lua` miteinander reden können (selbes Verzeichnis vielleicht?).     
3. CW üben und fröhlich sein. Zettel und Stift nicht vergessen!

## Verwendung

### Nur CW 

- `./cwkoch.lua -k4 -n60 | cw -w12`: Lektion 4 mit 60 Zeichen (wie im Kurs) und Geschwindigkeit 12w PARIS
- `./cwkoch.lua -alq -n60 | cw -w12`: Nur Buchstabe **_l_** und **_q_** für z.B. Einzeltraining
- `./cwkoch.lua -k8 -c50 -n60 | cw -w12 | `: Lektion 8, aber nur mit 50% Anteil des neuen Buchstabens **_t_** (c50). So kann man sich ran tasten.  
Parameter: 
- `-k`: sind die Lektionen von E13
- `-a`: lässt einzelne Buchstaben zu. So kann man sich seine eigene Reihenfolge zusammenstellen. Für häufigeres Vorkommen Buchstaben mehrfach angeben.
- `-n`: Geschwindigkeit. n60 sind 12 Gruppen bei 12WPM.
- `-c`: siehe Beispiel oben.

Ansonsten einfach mal die Hilfe von `cwkoch.lua` bemühen. Da gibt es bestimmt noch mehr.

### nato_tts.py

nato_tts.py macht aus den Buchstaben das ICAO Alphabet Nato-Alphabet und gibt das Ganze an die TTS-Engine `espeak-ng`.

* `./nato_tts.py`: Anschließend Text eingeben
* `./nato_tts.py Stefan`: ließt 'Stefan' vor
* `./nato_tts.py tmp_text.txt`: holt sich den Input aus einem File


Hier im Skript sind in der letzten Zeile die Parameter für `espeak-ng` wie , Stimme, Sprechgeschwindigkeit etc. gesetzt. Wenn Anpassungsbedarf besteht, hier schauen. 

### CW und TTS

Kombination von beiden und Ziel der Übung:

`./cwkoch.lua -k9 -n60 | cw -w12 | tee tmp_output.txt && ./nato_tts.py tmp_output.txt`

Schreibt den Output in die Textdatei 'tmp_output.txt' und bietet anschließend an das Ergebnis vorzulesen.

Für weitere Übungen einfach die cwkoch Parameter anpassen.

Ich habe für mich den letzten Befehl noch in ein `run.sh` script gepackt.

Viel Spaß!


