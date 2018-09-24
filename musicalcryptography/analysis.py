from music import *
import os

def get_note_list(score1):
   note_list2 = []
   phrase_list = []
   note_list = []
   part_list = []
   part_list = score.getPartList()
   for part in part_list:
      part1 = Part()
      part1 = part
      channel = part1.getChannel()
      if channel == 9:
         continue
      phrase_list = part1.getPhraseList()
      for phrase in phrase_list:
         phrase1 = Phrase()
         phrase1 = phrase
         note_list = phrase1.getNoteList()
         for note in note_list:
            note1 = Note(C4, HN)
            note1 = note
            if note1.getPitch() == -2147483648:
               continue
            else:
               note_list2.append(note1.getPitch())
   
   return note_list2


note_list3 = []
rootdir = "/home/lohith/Documents/Project/Music_Files"

for subdir, dirs, files in os.walk(rootdir):
   for file1 in files:
      score = Score()
      Read.midi(score, os.path.join(subdir, file1))
      note_list2 = get_note_list(score)
      note_list3.extend(note_list2)
            
f = open("note_list_Unsorted17.txt", "w")
f.write(str(note_list3))
f.close()


