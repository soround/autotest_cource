# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt
from string import digits


# Здесь пишем код

def read_data(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as file:
        result = file.read()
    return result


def save_to_file(filename: str, data: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)


def remove_digits(data: str) -> str:
    removed_digits = str.maketrans('', '', digits)
    result = data.translate(removed_digits)
    return result


raw_data = read_data('test_file/task1_data.txt')
formatted_data = remove_digits(raw_data)
save_to_file('test_file/task1_answer.txt', formatted_data)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
