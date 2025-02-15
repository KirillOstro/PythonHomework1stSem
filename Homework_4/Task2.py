import itertools


# 1. Создание бесконечного генератора чисел
def infinite_counter(start=0, step=1):
    return itertools.count(start, step)


# 2. Применение функций к каждому элементу в итераторе
def apply_function_to_iterable(iterable, func):
    return itertools.starmap(func, zip(iterable))


# 3. Объединение нескольких итераторов в один
def chain_iterables(*iterables):
    return itertools.chain(*iterables)


# Основная функция
if __name__ == "__main__":
    try:
        # 1. Бесконечный генератор чисел
        print("Бесконечный генератор чисел (первые 10 элементов):")
        counter = infinite_counter(10, 2)
        for _ in range(10):
            print(next(counter), end=" ")
        print("\n")

        # 2. Применение функции к каждому элементу итератора
        numbers = [1, 2, 3, 4, 5]
        print(f"Исходный список: {numbers}")
        squared_numbers = apply_function_to_iterable(numbers, lambda x: x**2)
        print("Квадраты элементов:", list(squared_numbers))

        # 3. Объединение нескольких итераторов
        iter1 = [1, 2, 3]
        iter2 = [4, 5, 6]
        iter3 = [7, 8, 9]
        print(f"\nИтератор 1: {iter1}")
        print(f"Итератор 2: {iter2}")
        print(f"Итератор 3: {iter3}")
        combined_iter = chain_iterables(iter1, iter2, iter3)
        print("Объединенный итератор:", list(combined_iter))

    except StopIteration:
        print("Ошибка: итератор пуст.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")