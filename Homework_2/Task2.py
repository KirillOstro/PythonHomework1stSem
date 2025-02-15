class DataBuffer:
    def __init__(self):
        self.buffer = []  # Инициализация пустого буфера

    def add_data(self, data):
        """Добавляет данные в буфер."""
        if len(self.buffer) >= 5:  # Проверка на переполнение буфера
            print("Переполнение буфера! Буфер будет очищен.")
            self.buffer.clear()  # Очистка буфера
        self.buffer.append(data)  # Добавление данных в буфер
        print(f"Данные '{data}' добавлены в буфер.")

    def get_data(self):
        """Получает данные из буфера."""
        if not self.buffer:  # Проверка, пуст ли буфер
            print("Буфер пуст. Нет данных для извлечения.")
            return None
        data = self.buffer.pop(0)  # Извлечение первого элемента из буфера
        print(f"Данные '{data}' извлечены из буфера.")
        return data

# Пример использования
if __name__ == "__main__":
    buffer = DataBuffer()  # Создаем объект буфера

    # Добавляем данные в буфер
    buffer.add_data("Данные 1")
    buffer.add_data("Данные 2")
    buffer.add_data("Данные 3")
    buffer.add_data("Данные 4")
    buffer.add_data("Данные 5")
    buffer.add_data("Данные 6")  # Вызовет переполнение и очистку буфера

    # Извлекаем данные из буфера
    print(buffer.get_data())  # Буфер пуст после переполнения
    buffer.add_data("Данные 7")
    print(buffer.get_data())
    print(buffer.get_data())  # Буфер снова пуст