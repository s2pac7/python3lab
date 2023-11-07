with open('F1.txt', 'w', encoding='utf-8') as file:
    while True:
        data = input("Введите данные: ")
        if not data:
            break
        file.write(data + '\n')

with open('F1.txt', 'r', encoding='utf-8') as f1, open('F2.txt', 'w', encoding='utf-8') as f2:
    lines = f1.readlines()
    for i, line in enumerate(lines):
        if i % 2 != 0:
            f2.write(line)

with open('F2.txt', 'r', encoding='utf-8') as file:
    first_line = file.readline()
    list_lines = list(first_line.split())
    word_count = len(list_lines)
    print("Количество слов в первой строке файла F2:", word_count)