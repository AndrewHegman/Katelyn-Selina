
import sys
# choice = int(input('1: Encrypt\n2: Decrypt\nChoose: '))
# message_input = input("message: ")
# shift = int(input("shift: "))
# aBcDeFgHiJkLmNoP
expected = 'bdfhj cegif dfheg'
choice = 1
message_input = 'abcde abcde abcde'
shift = [1, 2, 3, 4, 5]


def is_upper(letter):
    return ord(letter) <= 96


def encrypt(message):
    shift_index = 0
    # KEYWORD arguments
    print('encrypted: ', end='')
    for i in message:
        if i.isalpha():
            # Lower case
            if is_upper(i):
                i = ord(i) + shift[shift_index]
                while i > 90:
                    i -= 26
            # Upper case
            elif not is_upper(i):
                i = ord(i) + shift[shift_index]
                while i > 122:
                    i -= 26
        else:
            i = ord(i)
        shift_index += 1

        if shift_index > len(shift) - 1:
            shift_index = 0
        print(chr(i), end='')


def decrypt(message):
    shift_index = 0
    print('decrypted: ', end='')
    for i in message:
        if i.isalpha():
            if is_upper(i):
                max_letter = 65
            else:
                max_letter = 97

            letter_num = ord(i) - shift[shift_index]
            while letter_num < max_letter:
                letter_num += 26
        else:
            letter_num = ord(i)
        print(chr(letter_num), end='')


print(f'expected = {expected}')
if choice == 1:
    encrypt(message_input)

elif choice == 2:
    decrypt(message_input)




