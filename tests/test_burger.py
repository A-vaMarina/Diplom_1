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

    def test_set_buns_sets_bun(self, burger, mock_bun):
        """После вызова set_buns атрибут bun хранит переданную булочку."""
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_set_buns_overwrites_previous_bun(self, burger, mock_bun):
        """Повторный вызов set_buns заменяет предыдущую булочку."""
        burger.set_buns(mock_bun)
        mock_bun_next = Mock()
        burger.set_buns(mock_bun_next)
        assert burger.bun == mock_bun_next

    def test_add_ingredient_appends_ingredient(self, burger, mock_ingredient_sauce):
        """Ингредиент добавляется в конец списка ингредиентов."""
        burger.add_ingredient(mock_ingredient_sauce)
        assert burger.ingredients == [mock_ingredient_sauce]

    def test_remove_ingredient_by_index(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        """Ингредиент удаляется из списка по указанному индексу."""
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == [mock_ingredient_filling]

    
    
