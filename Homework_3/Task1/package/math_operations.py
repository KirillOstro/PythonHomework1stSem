class MathOperations:
    @staticmethod
    def sum_numbers(numbers):
        """
        Вычисляет сумму всех чисел в списке.

        :param numbers: Список чисел.
        :return: Сумма чисел.
        """
        if not isinstance(numbers, list):
            raise TypeError("Переданный аргумент должен быть списком.")
        return sum(numbers)
