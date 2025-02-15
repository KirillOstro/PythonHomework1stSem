from datetime import datetime, timedelta


# 1. Отображение текущей даты и времени
def show_current_datetime():
    now = datetime.now()
    print(f"Текущая дата и время: {now.strftime('%Y-%m-%d %H:%M:%S')}")


# 2. Вычисление разницы между двумя датами
def calculate_date_difference(date1, date2):
    difference = date2 - date1
    print(f"Разница между датами: {difference.days} дней")


# 3. Преобразование строки в объект даты и времени
def parse_string_to_datetime(date_string, format="%Y-%m-%d %H:%M:%S"):
    try:
        parsed_date = datetime.strptime(date_string, format)
        print(f"Преобразованная дата и время: {parsed_date}")
        return parsed_date
    except ValueError as e:
        print(f"Ошибка при преобразовании строки в дату: {e}")
        return None


# Основная функция
if __name__ == "__main__":
    # 1. Отображение текущей даты и времени
    show_current_datetime()

    # 2. Вычисление разницы между двумя датами
    date1 = datetime(2023, 10, 1)
    date2 = datetime(2023, 10, 15)
    print(f"\nДата 1: {date1.strftime('%Y-%m-%d')}")
    print(f"Дата 2: {date2.strftime('%Y-%m-%d')}")
    calculate_date_difference(date1, date2)

    # 3. Преобразование строки в объект даты и времени
    date_string = "2023-10-01 12:30:45"
    print(f"\nСтрока для преобразования: {date_string}")
    parsed_date = parse_string_to_datetime(date_string)
    if parsed_date:
        print(f"Преобразованная дата: {parsed_date.strftime('%Y-%m-%d %H:%M:%S')}")
        