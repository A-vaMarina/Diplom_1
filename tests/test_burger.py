from unittest.mock import Mock

import pytest


class TestBurger:

    def test_init_bun_is_none(self, burger):
        """После создания бургера булочка не установлена."""
        assert burger.bun is None

    def test_init_ingredients_is_empty_list(self, burger):
        """После создания бургера список ингредиентов пуст."""
        assert burger.ingredients == []

    def test_set_buns_bun_is_set(self, burger, mock_bun):
        """После вызова set_buns атрибут bun хранит переданную булочку."""
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_two_ingredients_second_added_to_end(
            self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        """Второй ингредиент добавляется в конец списка ингредиентов."""
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        assert burger.ingredients == [mock_ingredient_sauce, mock_ingredient_filling]

    @pytest.mark.parametrize("ingredient_fixture", ["mock_ingredient_sauce", "mock_ingredient_filling"])
    def test_add_ingredient_any_type_ingredient_added(self, burger, request, ingredient_fixture):
        """Ингредиент любого типа добавляется в список ингредиентов."""
        mock_ingredient = request.getfixturevalue(ingredient_fixture)
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient_middle_index_ingredient_removed(self, burger_with_ingredients, mock_ingredients):
        """Ингредиент из середины списка удаляется, остальные сохраняют порядок."""
        burger_with_ingredients.remove_ingredient(1)
        assert burger_with_ingredients.ingredients == [mock_ingredients[0], mock_ingredients[2]]

    @pytest.mark.parametrize(
        "index, new_index, expected_order",
        [
            (0, 2, [1, 2, 0]),  # вперёд: с начала в конец
            (2, 0, [2, 0, 1]),  # назад: с конца в начало
            (1, 1, [0, 1, 2]),  # на то же место, порядок не меняется
        ],
    )
    def test_move_ingredient_new_index_order_changed(
            self, burger_with_ingredients, mock_ingredients, index, new_index, expected_order):
        """Ингредиент перемещается на новую позицию, остальные сдвигаются."""
        burger_with_ingredients.move_ingredient(index, new_index)
        assert burger_with_ingredients.ingredients == [mock_ingredients[i] for i in expected_order]

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, total_price",
        [
            (100.0, [], 200.0),                # только булочка
            (100.0, [100.0], 300.0),           # булочка + 1 ингредиент
            (100.0, [100.0, 200.0], 500.0),    # булочка + 2 ингредиента
            (50.0, [10.0, 20.0, 30.0], 160.0), # булочка + 3 ингредиента
            (0.0, [], 0.0),                    # нулевая булочка
            (0.0, [0.0, 0.0], 0.0),            # все нули
            (12.5, [7.5, 5.0], 37.5),          # дробные цены
        ],
    )
    def test_get_price_buns_and_ingredients_total_price_calculated(
            self, burger, bun_price, ingredient_prices, total_price):
        """Цена бургера = цена булочки × 2 + сумма цен ингредиентов."""
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        for price in ingredient_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == total_price

    def test_get_receipt_buns_with_two_ingredients_receipt_formed(
            self, burger, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        """Чек содержит булочку, два ингредиента и цену."""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        receipt = (
            "(==== pink bun ====)\n"
            "= sauce berry sauce =\n"
            "= filling strawberry =\n"
            "(==== pink bun ====)\n"
            "\n"
            "Price: 550.0"
        )
        assert burger.get_receipt() == receipt
