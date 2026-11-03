from unittest.mock import Mock
import pytest

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    """Мок булочки с заданными именем и ценой"""
    mock_bun = Mock()
    mock_bun.get_name.return_value = "pink bun"
    mock_bun.get_price.return_value = 100.0
    return mock_bun

@pytest.fixture
def mock_ingredient_sauce():
    """Мок соуса"""
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = "berry sauce"
    mock_ingredient.get_price.return_value = 50.0
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock_ingredient


@pytest.fixture
def mock_ingredient_filling():
    """Мок начинки"""
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = "strawberry"
    mock_ingredient.get_price.return_value = 300.0
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock_ingredient

@pytest.fixture
def mock_ingredients():
    """Три разных мока ингредиентов для проверки удаления и перемещения"""
    return [Mock(), Mock(), Mock()]

@pytest.fixture
def burger_with_ingredients(burger, mock_ingredients):
    """Бургер с тремя добавленными ингредиентами из mock_ingredients"""
    for ingredient in mock_ingredients:
        burger.add_ingredient(ingredient)
    return burger
