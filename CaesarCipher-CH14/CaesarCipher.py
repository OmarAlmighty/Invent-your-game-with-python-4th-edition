# CESAR CIPHER
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)


def getmode():
    while True:
        print("Do you want to encrypt or decrypt")
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')


def getMessage():
    print("Entert your message")
    return input()


def getKey():
    key = 0
    while True:
        print("Enter the key number (1-%s)" % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


def getTranslatedMessage(mode, msg, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in msg:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:  # Symbol not found in SYMBOLS.
            # Just add this symbol without any change.
            translated += symbol
        else:
            # Encrypt or decrypt
            symbolIndex += key
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
            translated += SYMBOLS[symbolIndex]

    return translated


mode = getmode()
message = getMessage()
key = getKey()
print("Your translated text is:")
print(getTranslatedMessage(mode,message,key))