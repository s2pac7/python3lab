with open("Оценки.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        data = line.split()
        name = data[0]
        grades = list(map(int, data[1:]))
        average_grade = sum(grades) / len(grades)
        if average_grade > 8:
            print(data[0])
