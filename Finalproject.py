import sys

#My final project is to create a program that can encript and decript at the same time so I can secretly
#          pass notes to friend while we are having lecture without having the FBIs listening in.

translate = {
        'a': '1623', 'b': '2643', 'c': '3743', 'd': '4623', 'e': '2753', 'f': '2833', 'g': '9283',
        'h': '2382', 'i': '2832', 'j': '4832', 'k': '2342', 'l': '9872', 'm': '8242', 'n': '3822',
        'o': '6281', 'p': '7231', 'q': '1281', 'r': '2831', 's': '4721', 't': '2381', 'u': '7431',
        'v': '5480', 'w': '6200', 'x': '6960', 'y': '1920', 'z': '7920', ' ': '7390', ':': '7777',
        '.': '1111', "'": "5555", ',': '2323'
        
}

revtranslate = {
        '1623':'a', '2643':'b', '3743':'c', '4623':'d', '2753':'e', '2833':'f', '9283':'g',
        '2382':'h', '2832':'i', '4832':'j', '2342':'k', '9872':'l', '8242':'m', '3822':'n',
        '6281':'o', '7231':'p', '1281':'q', '2831':'r', '4721':'s', '2381':'t', '7431':'u',
        '5480':'v', '6200':'w', '6960':'x', '1920':'y', '7920':'y', '7390':' ', '7777':':',
        '1111':'.', "5555":"'", '2323':','

}

def readtext(file):
        with open(file) as text:
                msg = text.read().lower()
        return msg
        

def encryption(text):
        encrypted = ''
        for word in text:
                for letter in word:
                        for i in range(0,len(letter)):
                                x = letter[i]
                                if x in translate:       
                                        encrypted += translate[x]
                                else:   encrypted += letter
        return encrypted

def decryption(message):
        unencrypted = ''
        for i in range (0,len(message),4):
                block = message[int(i):int(i+4)]
                if block in revtranslate:
                        unencrypted += revtranslate[block]
        return unencrypted


def action():
        method = input('encrypt or decrypt: ')
        file = input('file name with extension: ')
        if method not in ('encrypt', 'decrypt'):
                print('Missing method, please choose to encrypt or decrypt')
        if method == 'encrypt':
                return print(encryption(readtext(file)))
        elif method == 'decrypt':
                return print(decryption(readtext(file)))
action()

"""
python3 Finalproject.py
       : decrypt   /    Transcript
       : encryptedsneakmessage.txt

"""
