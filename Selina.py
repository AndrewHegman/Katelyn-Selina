choice = 2
user_str = 'JGNNQ YQTNF'
output_str = ''
shift_amount = 54

if choice == 1:
    for letter in user_str:
        letter_num = ord(letter)
        letter_num += shift_amount

        while letter_num > 90:
            letter_num -= 26
        output_str += chr(letter_num)
    print('encrypted: ' + output_str)
elif choice == 2:
    for letter in user_str:
        letter_num = ord(letter)
        letter_num -= shift_amount

        while letter_num < 65:
            letter_num += 26
        output_str += chr(letter_num)
    print('decrypted: ' + output_str)

print('expected : JGNNQ YQTNF')


