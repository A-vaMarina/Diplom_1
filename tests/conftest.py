import pytest

from unittest.mock import Mock
from praktikum.burger import Burger


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
    mock_ingredient.get_type.return_value = "SAUCE"
    return mock_ingredient


@pytest.fixture
def mock_ingredient_filling():
    """Мок начинки"""
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = "strawberry"
    mock_ingredient.get_price.return_value = 300.0
    mock_ingredient.get_type.return_value = "FILLING"
    return mock_ingredient
