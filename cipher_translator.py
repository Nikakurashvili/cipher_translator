# cipher translator
# encrypts and decrypts text
# code has 3 functions:
# encode()- encrypts data
# decode()- decrypts data
# verify()- checks if functions work corectly 
# and compares input to output

# encryption is doen in 4 steps:
# 1- Caesar Shift — shift each letter by its position index 
# (0-based) in the string. So the 1st letter shifts by 0, 
# 2nd by 1, 3rd by 2, etc. Wrap around the alphabet. 
# Non-letters stay unchanged but still count toward the index.

# 2- Vowel Mirror — after shifting, replace each vowel (a,e,i,o,u) 
# with the "mirror" vowel: a↔u, e↔o, i↔i (stays). Case-sensitive 
# (uppercase mirrors uppercase).

# 3- Chunk & Reverse — split the result into chunks of 4 characters, 
# reverse each chunk, then join them back with a -.

# 4- Checksum Append — append #XY at the end where X = count of 
# letters, Y = count of non-letter/non-space characters in the 
# original string.



def encode(text):
    lower_letters = [chr(i+97) for i in range(26)]
    upper_letters = [chr(i+65) for i in range(26)]
    ceaser_shifted_text = ''
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                ceaser_shifted_text += upper_letters[(upper_letters.index(text[i])+i)%26]
            else:
                ceaser_shifted_text += lower_letters[(lower_letters.index(text[i])+i)%26]
        else:
            ceaser_shifted_text += text[i]

    vowel_mirror_text = ''
    for i in ceaser_shifted_text:
        if i == 'a':
            vowel_mirror_text += 'u'
        elif i == 'A':
            vowel_mirror_text += 'U'
        elif i == 'u':
            vowel_mirror_text += 'a'
        elif i == 'U':
            vowel_mirror_text += 'A'
        elif i == 'e':
            vowel_mirror_text += 'o'
        elif i == 'E':
            vowel_mirror_text += 'O'
        elif i == 'o':
            vowel_mirror_text += 'e'
        elif i == 'O':
            vowel_mirror_text += 'E'
        else:
            vowel_mirror_text += i

    chunk_and_reverse_text = []
    for i in range(0, len(vowel_mirror_text), 4):
        chunk_and_reverse_text.append(vowel_mirror_text[i:i+4][::-1])
    chunk_and_reverse_text = '-'.join(chunk_and_reverse_text)

    letter = ''
    non_letter = ''
    for i in text:
        if i.isalpha():
            letter += i
        elif not i.isalpha() and not i.isspace():
            non_letter += i
    checksum_append = f'{chunk_and_reverse_text}#{len(letter)},{len(non_letter)}'

    return checksum_append

print(encode('Hello, World!'))



def decode(text):

    text = text[:text.rfind('#')]

    chunk_and_reverse_text = ''
    text = ''.join(text.split('-'))
    for i in range(0, len(text), 4):
        chunk_and_reverse_text += text[i:i+4][::-1]

    vowel_mirror_text = ''
    for i in chunk_and_reverse_text:
        if i == 'a':
            vowel_mirror_text += 'u'
        elif i == 'A':
            vowel_mirror_text += 'U'
        elif i == 'u':
            vowel_mirror_text += 'a'
        elif i == 'U':
            vowel_mirror_text += 'A'
        elif i == 'e':
            vowel_mirror_text += 'o'
        elif i == 'E':
            vowel_mirror_text += 'O'
        elif i == 'o':
            vowel_mirror_text += 'e'
        elif i == 'O':
            vowel_mirror_text += 'E'
        else:
            vowel_mirror_text += i


    lower_letters = [chr(i+97) for i in range(26)]
    upper_letters = [chr(i+65) for i in range(26)]
    ceaser_shifted_text = ''
    for i in range(len(vowel_mirror_text)):
        if vowel_mirror_text[i].isalpha():
            if vowel_mirror_text[i].isupper():
                ceaser_shifted_text += upper_letters[(upper_letters.index(vowel_mirror_text[i])-i)%26]
            else:
                ceaser_shifted_text += lower_letters[(lower_letters.index(vowel_mirror_text[i])-i)%26]
        else:
            ceaser_shifted_text += vowel_mirror_text[i]

    return ceaser_shifted_text


print(decode('enfH-D ,s-evuw-!#10,2'))



def verify(text):

    return text == decode(encode(text))

print(verify("Hello, World!"))






