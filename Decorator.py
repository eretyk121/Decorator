import hashlib
import datetime

def logger(foo):
    def new_foo(*args):
        start_time = str(datetime.datetime.now())
        name_func = foo.__name__
        result = foo(*args)
        path_to_logs = input(f'Ввудите путь к файлу для записи логов: ')
        with open(path_to_logs, 'w', encoding='utf-8') as text:
            text.write(f'Начало работы функции {name_func} с аргументами {args}: {start_time}\n')
            text.write(f'Результат работы функции:\n')
            for one_line in result:
                text.writelines(f'{one_line}\n')
        return result
    return new_foo


@logger
def hash_text(path):
    with open(path, encoding='utf-8') as text:
        for line in text:
            md5_line = hashlib.md5(line.encode())
            yield md5_line.hexdigest()

if __name__ == '__main__':

    hash_text('DE.txt')

