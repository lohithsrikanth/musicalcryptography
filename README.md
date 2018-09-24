# musicalcryptography

This program lets you encrypt text to music and also enables decrypting from music to text.

Prerequisites:
1) Need to have the jythonMusic package which can be downloaded from https://jythonmusic.me/download/
2) Java version 8

Once the musicalcryptography folder is downloaded, transfer all files from this folder to the jythonMusic folder.

FOR LINUX and MAC: 
Encryption:
  1) Open the terminal
  2) Go to the jythonMusic folder
  3) Enter: python encryption.py
      Running this program enables the user to enter the text they want to encrypt
  4) Enter: sh jython.sh -i create_music.py
      This program will create a encryption.mid file which is a MIDI(musical) file which can now be exchanged.
      
Decryption:
  1) Do steps 1 and 2 from above
  2) Enter: sh jython.sh -i decrypt_music.py
  3) Enter: python decryption.py
      This program will allow you to see the text that was encrypted in the MIDI file that was exchanged.
      
FOR WINDOWS:
Encryption and decryption is same as Linux except instead of the command:
  sh jython.sh -i {filename}
Type:
  jython {filename}
