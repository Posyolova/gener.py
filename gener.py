q = [
    {'id': 1, 'full_name': 'Поселова Полина Вадимовна'},
    {'id': 2, 'full_name': 'Четверикова Олеся Александровна'},
    {'id': 3, 'full_name': 'Бобровская Анастасия Дмитриевна'}
    ]
w = [q['full_name'] for q in q if len(q['full_name'].split()[1]) > 6]
print(w)
