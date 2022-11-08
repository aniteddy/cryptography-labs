import os
from Crypto.Util import Counter
from Crypto.Cipher import AES

# интерфейс для функции блочного шифрования в режиме счетчика


# Шифрование
def enc(key, text):
    # Генерация строки случайных байтов
    iv = os.urandom(16)
    print('IV: ' + str(iv))
    # Счётчик + конвертирование iv в число
    ctr = Counter.new(128, initial_value=int(iv.hex(), AES.block_size))
    # Алгоритм AES
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return iv + aes.encrypt(text)


# Дешифрование
def dec(key, enc_text):
    # Инициализирующий вектор
    iv = enc_text[:16]
    # Счётчик
    count = Counter.new(128, initial_value=int(iv.hex(), AES.block_size))
    # Алгоритм AES
    aes = AES.new(key, AES.MODE_CTR, counter=count)
    return aes.decrypt(enc_text[16:])


def main():
    # Текст для шифрования
    text = b'black tigerblack tigerblack tigerblack tiger'
    print('Text: ' + str(text))

    # Генерация ключа, строка случайных байт
    key = os.urandom(32)
    print('Key: ' + str(key))

    # Зашифровать текст
    enc_text = enc(key, text)
    print('encrypted text: ' + str(enc_text))

    # Дешифровать текст
    dec_text = dec(key, enc_text)
    print('decrypted text: ' + str(dec_text))


if __name__ == '__main__':
    main()
