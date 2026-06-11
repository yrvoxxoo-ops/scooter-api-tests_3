import allure

from helpers import generate_courier_data
from courier_methods import CourierMethods


@allure.epic("Курьер")
@allure.feature("Логин курьера")
class TestLoginCourier:
    @allure.title("Успешный логин курьера")
    def test_login_courier_success(self):

        payload = generate_courier_data()
        CourierMethods.create_courier(payload)
        login_data = {"login": payload["login"], "password": payload["password"]}
        response = CourierMethods.login_courier(login_data)
        assert response.status_code == 200
        assert "id" in response.json()
    
    @allure.title("Нельзя войти без логина")
    def test_login_courier_without_login(self):
        payload = generate_courier_data()
        CourierMethods.create_courier(payload)
        login_data = {"login": "", "password": payload["password"]}
        response = CourierMethods.login_courier(login_data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"


    @allure.title("Нельзя войти без пароля")
    def test_login_courier_without_password(self):
        payload = generate_courier_data()
        CourierMethods.create_courier(payload)
        login_data = {"login": payload["login"],"password": ""}
        response = CourierMethods.login_courier(login_data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"
    
    @allure.title("Нельзя войти с неверным логином")
    def test_login_courier_with_wrong_login(self):
        payload = generate_courier_data()
        CourierMethods.create_courier(payload)
        login_data = {"login": "wrong_login", "password": payload["password"]}
        response = CourierMethods.login_courier(login_data)
        assert response.status_code == 404


    @allure.title("Нельзя войти с неверным паролем")
    def test_login_courier_with_wrong_password(self):
        payload = generate_courier_data()
        CourierMethods.create_courier(payload)
        login_data = {"login": payload["login"], "password": "wrong_password"}
        response = CourierMethods.login_courier(login_data)
        assert response.status_code == 404 