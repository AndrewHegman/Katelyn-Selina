LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(message, key):
    encrypted = ''
    for chars in message:
        if chars.isalpha():
            num = LETTERS.find(chars)
            print(num)
            num += key
            encrypted += LETTERS[num]
    return encrypted


def decrypt(message, key):
    decrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num -= key
            decrypted += LETTERS[num]

    return decrypted


def main():
    message = str(input('Enter your message: '))
    key = int(input('Enter you shift amount: '))
    choice = input('Encrypt or Decrypt? enter e for encryption, d for decryption: ')

    if choice.lower().startswith('e'):
        print(encrypt(message, key))
    else:
        print(decrypt(message, key))


if __name__ == '__main__':
    main()