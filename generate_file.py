#!/usr/bin/env python3
import random
import string
import sys

def generate_random_file(filename):
    # Генерируем 50 случайных символов
    chars = ''.join(random.choices(
        string.ascii_letters + string.digits,
        k=50
    ))

    # Записываем в файл
    with open(filename, 'w') as f:
        f.write(chars + '\n')

    print(f'✅ Файл {filename} создан с содержимым: {chars}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Использование: python3 generate_file.py <имя_файла>")
        sys.exit(1)

    filename = sys.argv[1]
    generate_random_file(filename)
