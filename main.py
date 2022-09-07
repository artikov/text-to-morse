#Dictionary that represents MORSE CODE (ITU)
MORSE_DICT = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    code = ''
    for l in message:
        if l != ' ':
            code += MORSE_DICT[l.upper()] + ' '
        else:
            code += ' '

    return code


def decrypt(code):
    message = ''
    morse_letters = code.split(' ')
    print(morse_letters)
    for l in morse_letters:
        if l != '':
            message += list(MORSE_DICT.keys())[list(MORSE_DICT.values()).index(l)]
        else:
            message += ' '
    return message


def main():
    print('||| Text to Morse Translator |||')
    crypt = input('Would you like to encrypt or decrypt? (e for encrypt & d for decrypt)\n')

    if crypt != 'e' and crypt != 'd':
        print('Wrong option.')

    if crypt == 'e':
        message = input('Enter the message that you would like to translate into Morse Code:\n')
        result = encrypt(message)
        print(result)

    if crypt == 'd':
        code = input('Enter the code that you would like to decrypt:\n')
        result = decrypt(code)
        print(result)


if __name__ == '__main__':
    main()
