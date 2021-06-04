import sys
# choice = int(input('1: Encrypt\n2: Decrypt\nChoose: '))
# message_input = input("message: ")
# shift = int(input("shift: "))
# aBcDeFgHiJkLmNoP
expected = 'aBcDeFgHiJkLmNoP'
choice = 2
message_input = 'eFgHiJkLmNoPqRsT'
shift = 30

def is_upper(letter):
    return ord(letter) <= 96

def encrypt(message):
    # KEYWORD arguments
    print('encrypted: ', end='')
    for i in message:
        # Lower case
        if is_upper(i):
            i = ord(i) + shift
            while i > 90:
                i -= 26
            print(chr(i), end='')
        # Upper case
        elif not is_upper(i):
            i = ord(i) + shift
            while i > 122:
                i -= 26
            print(chr(i), end='')


def decrypt(message):
    print('decrypted: ', end='')
    for i in message:
        if is_upper(i):
            max_letter = 65
        else:
            max_letter = 97

        letter_num = ord(i) - shift
        while letter_num < max_letter:
            letter_num += 26
        print(chr(letter_num), end='')


print(f'expected = {expected}')
if choice == 1:
    encrypt(message_input)

elif choice == 2:
    decrypt(message_input)




