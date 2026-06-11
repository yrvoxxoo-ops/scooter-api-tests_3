import allure
from order_methods import OrderMethods

@allure.epic("Заказ")
@allure.feature("Список заказов")
class TestGetOrders:

    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        response = OrderMethods.get_orders()
        assert response.status_code == 200
        assert "orders" in response.json()