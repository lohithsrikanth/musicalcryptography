#!/usr/bin/env python

from music import *

score = Score()
Read.midi(score, "encryption.mid")

def get_note_and_channel_list(score1):
    note_list2 = []
    channel_list = []
    phrase_list = []
    note_list = []
    part_list = []
    note_and_channel_list = []
    part_list = score.getPartList()
    for part in part_list:
       part1 = Part()
       part1 = part
       channel = part1.getChannel()
       channel_list.append(channel)
       phrase_list = part1.getPhraseList()
       for phrase in phrase_list:
          phrase1 = Phrase()
          phrase1 = phrase
          note_list = phrase1.getNoteList()
          for note in note_list:
             note1 = Note(C4, HN)
             note1 = note
             note_list2.append(note1.getPitch())
   
    for i in range(len(note_list2)):
        tuple1 = (note_list2[i], channel_list[i])
        note_and_channel_list.append(tuple1)
        
    return note_and_channel_list

decrypted_notes = get_note_and_channel_list(score)
f = open("decrypted_notes.txt", "w")
f.write(str(decrypted_notes))
f.close()