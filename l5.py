import base64
import rsa


# генерация ключей
def key_gen():
    key = rsa.newkeys(4096)
    print('Keys: ' + str(key))
    return key


# проверка подписи
def verify(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature, key) == 'SHA-256'
    except:
        return False


# генерация подписи
def sign(message, key):
    signature = rsa.sign(message.encode('ascii'), key, 'SHA-256')
    return signature


def main():
    # текст для подписи
    text = 'black tiger'
    print('Text: ' + text)
    (public_key, private_key) = key_gen()

    # подпись
    signature = sign(text, private_key)
    signature_convert = base64.b64encode(signature).decode('utf8')
    print('Signature: ' + str(signature_convert))

    # Проверка действительна ли подпись
    verified = verify(text, base64.b64decode(signature_convert), public_key)
    print('Verify: ' + str(verified))

    # поддельная подпись
    # text2 = 'white tiger'
    # verified = verify(text2, base64.b64decode(signature_convert), public_key)
    # print('Text 2: ' + text2)
    # print('Verify: ' + str(verified))


if __name__ == '__main__':
    main()
