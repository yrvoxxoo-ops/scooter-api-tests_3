import allure

from helpers import generate_courier_data
from courier_methods import CourierMethods


@allure.epic("Курьер")
@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        payload = generate_courier_data()
        response = CourierMethods.create_courier(payload)
        assert response.status_code == 201
        assert response.json()["ok"] is True

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self):
        payload = generate_courier_data()
        CourierMethods.create_courier(payload)
        response = CourierMethods.create_courier(payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Нельзя создать курьера без логина")
    def test_create_courier_without_login(self):
        payload = generate_courier_data()
        payload.pop("login")
        response = CourierMethods.create_courier(payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Нельзя создать курьера без пароля")
    def test_create_courier_without_password(self):
        payload = generate_courier_data()
        payload.pop("password")
        response = CourierMethods.create_courier(payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"