try:
    with open('Часы.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    subject_dict = {}

    for line in lines:
        parts = line.split(':')
        if len(parts) == 2:
            subject_name = parts[0].strip()
            info = parts[1].strip()

            import re
            lectures = re.search(r'(\d+)\(л\)', info)
            practices = re.search(r'(\d+)\(пр\)', info)
            labs = re.search(r'(\d+)\(лаб\)', info)

            if lectures:
                total_lectures = int(lectures.group(1))
            else:
                total_lectures = 0

            if practices:
                total_practices = int(practices.group(1))
            else:
                total_practices = 0

            if labs:
                total_labs = int(labs.group(1))
            else:
                total_labs = 0

            total_classes = total_lectures + total_practices + total_labs

            subject_dict[subject_name] = total_classes

    for subject, total_classes in subject_dict.items():
        print(subject, ":", total_classes)

except IOError:
    print("Произошла ошибка ввода-вывода!")

