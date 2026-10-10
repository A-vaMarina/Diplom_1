import pytest

from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    def test_init_bun_is_none(self, burger):
        """После создания бургера булка не установлена."""
        assert burger.bun is None

    def test_init_ingredients_is_empty_list(self, burger):
        """После создания бургера список ингредиентов пуст."""
        assert burger.ingredients == []

    def test_set_buns_bun_is_set(self, burger, mock_bun):
        """После вызова set_buns атрибут bun хранит переданную булочку."""
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_two_ingredients_second_added_to_end(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        """Второй ингредиент добавляется в конец списка ингредиентов."""
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        assert burger.ingredients == [mock_ingredient_sauce, mock_ingredient_filling]

    def test_remove_ingredient_zero_index_ingredient_removed(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        """Ингредиент с индексом 0 удаляется из списка."""
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == [mock_ingredient_filling]

    def test_move_ingredient_second_to_first_order_changed(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        """Второй ингредиент перемещается на первую позицию в списке."""
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [mock_ingredient_filling, mock_ingredient_sauce]    

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
    def test_get_price_buns_and_ingredients_total_price_calculated(self, burger, bun_price, ingredient_prices, total_price):
        """Цена бургера = цена булочки × 2 + сумма цен ингредиентов."""
        
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == total_price

    def test_get_receipt_buns_with_two_ingredients_receipt_formed(self, burger, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
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
