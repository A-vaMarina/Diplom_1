## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие класс `Burger`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` — пакет, содержащий код программы.
- `tests` — пакет, содержащий тесты, покрывающие класс `Burger` (файл `test_burger.py`).
- `htmlcov` — папка с HTML-отчётом о покрытии.

### Описание тестов

- `test_init_bun_is_none` — проверяет, что после создания бургера булочка не установлена.
- `test_init_ingredients_is_empty_list` — проверяет, что после создания бургера список ингредиентов пуст.
- `test_set_buns_bun_is_set` — проверяет, что после вызова `set_buns` атрибут `bun` хранит переданную булочку.
- `test_add_ingredient_two_ingredients_second_added_to_end` — проверяет, что второй ингредиент добавляется в конец списка ингредиентов.
- `test_remove_ingredient_zero_index_ingredient_removed` — проверяет, что ингредиент с индексом 0 удаляется из списка.
- `test_move_ingredient_second_to_first_order_changed` — проверяет, что второй ингредиент перемещается на первую позицию в списке.
- `test_get_price_buns_and_ingredients_total_price_calculated` — проверяет, что цена бургера равна цене булочки × 2 плюс сумма цен ингредиентов (параметризованный тест).
- `test_get_receipt_buns_with_two_ingredients_receipt_formed` — проверяет, что чек содержит булочку, два ингредиента и цену.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest tests/test_burger.py --cov=praktikum.burger --cov-report=term-missing --cov-report=html`
