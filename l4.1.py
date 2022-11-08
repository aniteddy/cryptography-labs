from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh


def key_gen():
    # Генерация ключа, строка случайных байт
    key = dh.generate_parameters(generator=2, key_size=512, backend=default_backend())
    print('Key: ' + str(key))
    return key


# генерация ключевой пары алисой
def aliceGen(param):
    alice_private = param.generate_private_key()
    alice_public = alice_private.public_key()
    return alice_private, alice_public


# генерация ключевой пары бобом
def bobGen(param):
    bob_private = param.generate_private_key()
    bob_public = bob_private.public_key()
    return bob_private, bob_public


# вычисление общего ключа Алисой
def aliceDerive(alice_private, bob_public):
    alice_shared = alice_private.exchange(bob_public)
    return alice_shared


# Вычисление общего ключа бобом
def bobDerive(bob_private, alice_public):
    bob_shared = bob_private.exchange(alice_public)
    return bob_shared


def verify_key(alice_shared, bob_shared):
    if alice_shared == bob_shared:
        b = True
    else:
        b = False
    return b


def main():
    param = key_gen()

    # ключевая пара алисы
    alice_private, alice_public = aliceGen(param)
    print('Alice private key: ' + str(alice_private))
    print('Alice public key: ' + str(alice_public))

    # ключевая пара боба
    bob_private, bob_public = bobGen(param)
    print('Bob private key: ' + str(bob_private))
    print('Bob public key: ' + str(bob_public))

    # общий ключ алисы
    alice_shared = aliceDerive(alice_private, bob_public)
    print("Alice shared: " + str(alice_shared))

    # общий ключ боба
    bob_shared = bobDerive(bob_private, alice_public)
    print("Bob shared: " + str(bob_shared))

    # проверка совпадают ли полученные ключи алисы и боба
    verify = verify_key(alice_shared, bob_shared)
    print("Verify: " + str(verify))


if __name__ == '__main__':
    main()