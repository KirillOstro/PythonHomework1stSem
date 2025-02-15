def read_numeric_lines(file_name):
    try:

        with open(file_name, 'r', encoding='utf-8') as file:
            data = file.readlines()

        for line in data:

            stripped_line = line.strip()

            try:
                number = float(stripped_line)
                print(number)
            except ValueError:

                raise TypeError(f"Ошибка: '{stripped_line}' не является числом")

    except FileNotFoundError:

        raise FileNotFoundError(f"Файл '{file_name}' не найден")


# Пример использования
if __name__ == "__main__":
    file_name = 'data.txt'  # Имя файла
    try:
        read_numeric_lines(file_name)
    except FileNotFoundError as e:
        print(e)
    except TypeError as e:
        print(e)