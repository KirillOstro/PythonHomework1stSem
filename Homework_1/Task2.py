import logging

# Настройка логирования
logging.basicConfig(filename='warehouse.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Класс Товар
class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        logging.info(f"Создан товар: {self.name}, количество: {self.quantity}, цена: {self.price}")

    def increase_quantity(self, amount):
        """Увеличивает количество товара"""
        self.quantity += amount
        logging.info(f"Увеличение количества товара {self.name} на {amount}. Новое количество: {self.quantity}")

    def decrease_quantity(self, amount):
        """Уменьшает количество товара"""
        if self.quantity >= amount:
            self.quantity -= amount
            logging.info(f"Уменьшение количества товара {self.name} на {amount}. Новое количество: {self.quantity}")
        else:
            logging.warning(f"Недостаточно товара {self.name} для уменьшения на {amount}")

    def calculate_cost(self):
        """Рассчитывает стоимость товара"""
        return self.quantity * self.price

# Класс Склад
class Warehouse:
    def __init__(self):
        self.products = []
        logging.info("Создан новый склад")

    def add_product(self, product):
        """Добавляет товар на склад"""
        self.products.append(product)
        logging.info(f"Товар {product.name} добавлен на склад")

    def remove_product(self, product_name):
        """Удаляет товар со склада"""
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                logging.info(f"Товар {product_name} удален со склада")
                return
        logging.warning(f"Товар {product_name} не найден на складе")

    def calculate_total_cost(self):
        """Рассчитывает общую стоимость всех товаров на складе"""
        total_cost = sum(product.calculate_cost() for product in self.products)
        logging.info(f"Общая стоимость товаров на складе: {total_cost}")
        return total_cost

# Класс Продавец
class Seller:
    def __init__(self, name):
        self.name = name
        self.sales_report = []
        logging.info(f"Создан продавец: {self.name}")

    def sell_product(self, product, quantity, warehouse):
        """Продает товар и обновляет склад"""
        if product in warehouse.products:
            if product.quantity >= quantity:
                product.decrease_quantity(quantity)
                total_cost = quantity * product.price
                self.sales_report.append((product.name, quantity, total_cost))
                logging.info(f"Продавец {self.name} продал {quantity} единиц товара {product.name} на сумму {total_cost}")
            else:
                logging.warning(f"Недостаточно товара {product.name} для продажи")
        else:
            logging.warning(f"Товар {product.name} отсутствует на складе")

    def get_sales_report(self):
        """Возвращает отчёт о продажах"""
        logging.info(f"Продавец {self.name} запросил отчёт о продажах")
        return self.sales_report

# Пример использования
if __name__ == "__main__":
    # Создаем товары
    product1 = Product("Яблоки", 100, 50)
    product2 = Product("Бананы", 200, 30)

    # Создаем склад и добавляем товары
    warehouse = Warehouse()
    warehouse.add_product(product1)
    warehouse.add_product(product2)

    # Создаем продавца
    seller = Seller("Иван")

    # Продаем товары
    seller.sell_product(product1, 10, warehouse)
    seller.sell_product(product2, 50, warehouse)

    # Выводим отчёт о продажах
    print("Отчёт о продажах:")
    for item in seller.get_sales_report():
        print(f"Товар: {item[0]}, Количество: {item[1]}, Стоимость: {item[2]}")

    # Выводим общую стоимость товаров на складе
    print(f"Общая стоимость товаров на складе: {warehouse.calculate_total_cost()}")