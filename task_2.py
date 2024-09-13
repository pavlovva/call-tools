data = [
    "Андрей 9",
    "Василий 11",
    "Роман 7",
    "X Æ A-12 45",
    "Иван Петров 3",
    "Андрей 6",
    "Роман 11",
    "Джон Доу 0",
    "Александр IV 8",
    "Алексей Иванович Петрович 15",
    "Пупа 5",
    "Лупа 5",
    "Лупа 14",
    "X Æ A-12 10",
    "!@#$%^&*()_+ 12",
    "Антоха -2",
    "  ",
]

# предположу что отрицательные числа допустимы, и Антоха работал -2 часа

workers = {}

for entry in data:
    entry = entry.strip()
    if not entry:
        continue

    parts = entry.split()
    if len(parts) < 2:
        print("Ошибка ввода: недостаточно данных")
        continue

    *name_parts, hours = parts
    name = ' '.join(name_parts)

    try:
        hours = int(hours)
    except ValueError:
        print(f"Ошибка ввода: неверное значение часов '{hours}' для {name}")
        continue

    if name in workers:
        workers[name].append(hours)
    else:
        workers[name] = [hours]

for name, hours_list in workers.items():
    total_hours = sum(hours_list)
    hours_str = ', '.join(map(str, hours_list))
    print(f"{name}: {hours_str}; sum: {total_hours}")
