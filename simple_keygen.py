import random
"""
V*ry PDF Ed*t*r key generator.
"""
def fix_digits(a: int, b: int) -> list:
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return ["Hata: Geçersiz giriş. Lütfen tam sayılar girin."]
    temp_a = max(a, b)
    temp_b = min(a, b)
    if temp_a + temp_b == 10:
        return [temp_a, temp_b]
    elif temp_a == temp_b and temp_a + temp_b > 10:
        eksik = 10 - temp_b
        temp_b = eksik
        return [temp_a, temp_b]
    elif temp_a + temp_b > 10:
        fazla = (temp_a + temp_b) - 10
        temp_a -= fazla
        return [temp_a, temp_b]
    else:
        eksik = 10 - (temp_a + temp_b)
        temp_b += eksik
        return [temp_a, temp_b]

def gen_key(length: int) -> str:
    characters = [1,2,3,4,5,6,7,8,9]
    key = [random.choice(characters) for _ in range(length)]
    return key

def main():
    key = gen_key(16)
    print("Oluşturulan anahtar:", key)
    ilk = fix_digits(key[0], key[15])
    key[0] = ilk[0]
    key[15] = ilk[1]
    iki = fix_digits(key[1], key[14])
    key[1] = iki[0]
    key[14] = iki[1]
    key[2] = 4
    key[3] = 1
    key[5] = 'A'
    print("Düzeltilmiş anahtar:", key)
    return ''.join(map(str, key))

if __name__ == "__main__":
    main()
