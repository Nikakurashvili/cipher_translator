# cipher_translator
Text-based encryption and decryption tool built with Python.

# what you can do in the project
- encrypt text using a multi-step cipher system
- decrypt encoded text back to original form
- verify that encryption and decryption work correctly

# how encryption works
- encryption is done in 4 steps

Caesar Shift — 
shift each letter by its position index 
(0-based) in the string. So the 1st letter shifts by 0, 
2nd by 1, 3rd by 2, etc. Wrap around the alphabet. 
Non-letters stay unchanged but still count toward the index.

Vowel Mirror — 
after shifting, replace each vowel (a,e,i,o,u) 
with the "mirror" vowel: a↔u, e↔o, i↔i (stays). Case-sensitive 
(uppercase mirrors uppercase).

Chunk & Reverse — 
split the result into chunks of 4 characters, 
# reverse each chunk, then join them back with a -.

Checksum Append — append #XY at the end where X = count of 
letters, Y = count of non-letter/non-space characters in the 
original string.

# How to Run
```
git clone https://github.com/Nikakurashvili/cipher_translator.git
cd cipher-translator
python main.py
```
