# генерация ключевой пары алисой
def aliceGen(g, p):
    a = 41
    alice_key = g ** a % p
    return a, alice_key


# генерация ключевой пары
def bobGen(g, p):
    b = 12
    bob_key = g ** b % p
    return b, bob_key


# вычисление общего ключа Алисой
def aliceDerive(a, bob_key, p):
    kA = bob_key**a % p
    return kA


# Вычисление общего ключа бобом
def bobDerive(b, alice_key, p):
    kB = alice_key**b % p
    return kB


# ассёрт на равенство полученных ключей в
def keyVerif(kA, kB):
    if kA == kB:
        return True
    else:
        return False


def main():
    p = 3001  # простое число, лучше большое, в котором много вариантов других
    g = 2  # натуральное число (любое)
    # если условие не выполняется, то протокол диффи-хеллмана не сработает, поэтому p простое
    if g**(p-1)%p != 1:
        raise SystemExit
    a, alice_key = aliceGen(g, p)
    print('Alice key: ' + str(alice_key))
    b, bob_key = bobGen(g, p)
    print('Bob key: ' + str(bob_key))
    kA = aliceDerive(a, bob_key, p)
    print('Alice derive: ' + str(kA))
    kB = bobDerive(b, alice_key, p)
    print('Bob derive: ' + str(kB))
    print('Verify: ' + str(keyVerif(kA, kB)))


if __name__ == '__main__':
    main()