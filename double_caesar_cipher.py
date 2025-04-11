def caesar_shift(text, shift):
    ukr_lower = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    ukr_upper = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    result = ""
    for char in text:
        if char in ukr_lower:
            index = (ukr_lower.find(char) + shift) % len(ukr_lower)
            result += ukr_lower[index]
        elif char in ukr_upper:
            index = (ukr_upper.find(char) + shift) % len(ukr_upper)
            result += ukr_upper[index]
        else:
            result += char
    return result

def encrypt(text, key1, key2):
    first_shift = caesar_shift(text, key1)
    second_shift = caesar_shift(first_shift, key2)
    return second_shift

def decrypt(text, key1, key2):
    first_shift = caesar_shift(text, -key2)
    second_shift = caesar_shift(first_shift, -key1)
    return second_shift

def main():
    text = input("Введіть текст для шифрування: ")
    key1 = int(input("Введіть перший ключ (зсув): "))
    key2 = int(input("Введіть другий ключ (зсув): "))

    encrypted_text = encrypt(text, key1, key2)
    print(f"Зашифрований текст: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text, key1, key2)
    print(f"Розшифрований текст: {decrypted_text}")

if __name__ == "__main__":
    main()
