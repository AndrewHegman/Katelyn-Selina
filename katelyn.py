import sys
# choice = int(input('1: Encrypt\n2: Decrypt\nChoose: '))
# message_input = input("message: ")
# shift = int(input("shift: "))
expected = 'aBcDeFgHiJkLmNoP'
choice = 2
message_input = 'eFgHiJkLmNoPqRsT'
shift = 30


def encrypt(message):
    # KEYWORD arguments
    print('encrypted: ', end='')
    for i in message:
        i = ord(i) + shift
        while i > 122:
            i -= 27
        print(chr(i), end='')


def decrypt(message):
    print('decrypted: ', end='')
    for i in message:
        letter_num = ord(i) - shift
        while letter_num < 97:
            letter_num += 26
        print(chr(letter_num), end='')


print(f'expected = {expected}')
if choice == 1:
    encrypt(message_input)

elif choice == 2:
    decrypt(message_input)
