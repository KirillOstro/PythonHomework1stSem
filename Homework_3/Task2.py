from collections import Counter
import string


def count_unique_words(text):
    # Удаляем знаки препинания из текста
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Разделяем текст на слова (игнорируем пробелы)
    words = text.lower().split()

    # Используем Counter для подсчета уникальных слов
    word_counts = Counter(words)

    # Возвращаем количество уникальных слов
    return len(word_counts)


# Пример использования
if __name__ == "__main__":
    text = "Hello, world! Hello, everyone. This is a test: test, test, test!"
    unique_words_count = count_unique_words(text)
    print(f"Количество уникальных слов: {unique_words_count}")
