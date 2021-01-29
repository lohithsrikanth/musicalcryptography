#!/usr/bin/env python
from music import *

f = open("playable_notes.txt", "r")
playable_notes = eval(f.read())
f.close()

f = open("playable_channels.txt", "r")
playable_channels = eval(f.read())
f.close()

f = open("duration_list.txt", "r")
duration_list = eval(f.read())
f.close()

f = open("dynamics_list.txt", "r")
dynamics_list = eval(f.read())
f.close()

score = Score("Encryption Music", 220.0)
i = 0
for i in range(len(playable_notes)):
    if playable_notes[i] == -46:
        note = Note(abs(playable_notes[i]), duration_list[i], dynamics_list[i])
    elif playable_notes[i] == -44:
        note = Note(abs(playable_notes[i]), duration_list[i], dynamics_list[i])
    elif playable_notes[i] == -33:
        note = Note(abs(playable_notes[i]), duration_list[i], dynamics_list[i])
    elif playable_notes[i] == -63:
        note = Note(abs(playable_notes[i]), duration_list[i], dynamics_list[i])
    elif playable_notes[i] == -58:
        note = Note(abs(playable_notes[i]), duration_list[i], dynamics_list[i])
    elif playable_notes[i] == -59:
        note = Note(abs(playable_notes[i]), duration_list[i], dynamics_list[i])
    
    else:
        note = Note(playable_notes[i], duration_list[i], dynamics_list[i])
    if i == 0:
        phrase = Phrase(float(i))
    else:
        phrase = Phrase(float(i) + 1.0)
    phrase.addNote(note)
    part = Part(GUITAR, playable_channels[i])
    part.addPhrase(phrase)
    score.addPart(part)
    
Write.midi(score, "encryption.mid")
Play.midi(score)
