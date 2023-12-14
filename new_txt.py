def is_closed(file_):
    """
    Функция принимает объект файл и проверяет его состояние
    """
    if file_.closed:
        print('Файл закрыт')
    else:
        print('Файл открыт')

files = [
    {'name': '1.txt', 'lines': []},
    {'name': '2.txt', 'lines': []},
    {'name': '3.txt', 'lines': []}
    ]
for file in files:
    with open(file['name'], encoding = 'utf-8') as f:
        file['lines'] = f.readlines()
        file['line_count'] = len(file['lines'])

sorted_files = sorted(files, key = lambda x: x['line_count'])

with open('new.txt', 'w', encoding = 'utf-8') as new_f:
    for file in sorted_files:
        new_f.write(file['name'] + '\n')
        new_f.write(str(file['line_count']) + '\n')
        new_f.writelines(file['lines'])
        new_f.write('\n')

is_closed(f)
is_closed(new_f)

