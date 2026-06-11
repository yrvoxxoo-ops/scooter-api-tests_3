import allure
import pytest

from data import order_data 
from order_methods import OrderMethods


@allure.epic("Заказ")
@allure.feature("Создание заказа")
class TestCreateOrder:

    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    @allure.title("Создание заказа с разными цветами")
    def test_create_order_with_different_colors(self, color):
        payload = order_data.copy()
        payload["color"] = color
        response = OrderMethods.create_order(payload)
        assert response.status_code == 201
        assert "track" in response.json()