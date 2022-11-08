import hmac
import hashlib

import os


def key_gen():
    # Генерация ключа, строка случайных байт
    key = os.urandom(32)
    print('Key: ' + str(key))
    return key


# Генерация МАКа s под ключом key для сообщения text
def sign(key, text):
    hmac_digest = hmac.new(key, text.encode(), hashlib.sha256).digest()
    print('Digest: ' + str(hmac_digest))
    return hmac_digest


# Верификация МАКа s сообщения text
def verify(key, s, text):
    hmac_digest = hmac.new(key, text.encode(), hashlib.sha256).digest()
    return hmac.compare_digest(s, hmac_digest)


def main():
    text = 'black tiger'
    wrongtext = 'white tiger'
    print('Text: ' + str(text))
    print('Wrong text: ' + str(wrongtext))
    # генерация ключа
    key = key_gen()
    s = sign(key, text)
    # проверка правильного сообщения
    v = verify(key, s, text)
    print('Verify: ' + str(v))
    # проверка неправильного сообщения
    v2 = verify(key, s, wrongtext)
    print('Verify2: ' + str(v2))


if __name__ == '__main__':
    main()
