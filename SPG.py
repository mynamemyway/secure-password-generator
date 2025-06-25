from random import sample as sample

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."
answer = 'Введите "y" для подтверждения или любую другую клавишу, чтобы отказаться >'
chars = ""


def hello():
    print("-" * 37)
    print("Добро пожаловать в генератор паролей!")
    print("-" * 37)
    print("Укажите требуемые параметры для генерации:")
    print()


def is_chars():
    global chars
    print(f"Включать ли цифры 0123456789?\n{answer}")
    if input() == "y":
        chars += digits
        print("Цифры включены в генератор", "\n")
    print(f"Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ\n{answer}")
    if input() == "y":
        chars += uppercase_letters
        print("Прописные буквы включены в генератор", "\n")
    print(f"Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?\n{answer}")
    if input() == "y":
        chars += lowercase_letters
        print("Строчные буквы включены в генератор", "\n")
    print(f"Включать ли символы !#$%&*+-=?@^_?\n{answer}")
    if input() == "y":
        chars += punctuation
        print("Символы !#$%&*+-=?@^_? включены в генератор", "\n")
    print(f"Исключать ли неоднозначные символы il1Lo0O?\n{answer}")
    if input() == "y":
        for s in "il1Lo0O":
            chars = chars.replace(s, "")
    if chars == "":
        print(
            "\n",
            "Error",
            "\n",
            "Параметры не заданы, вернитесь и выберите символы для генерации:",
            "\n",
        )
        is_chars()
    return chars


def is_your_passwords(s, n, c):
    print(f"\nПароли по заданным параметрам успешно сгенерированы:")
    passwords = ["".join(sample(s, n)) for p in range(c)]
    return passwords


hello()
is_chars()
print("Введите длину пароля и количество вариаций:")
print(*is_your_passwords(chars, int(input()), int(input())), sep="\n")
