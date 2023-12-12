def is_closed(file_):
    """
    Функция принимает объект файл и проверяет его состояние
    """
    if file_.closed:
        print('Файл закрыт')
    else:
        print('Файл открыт')

with open('1.txt', 'r') as f:
    lines = f.readlines()
    count = len(lines)
    print('Количество строк в файле:', count)