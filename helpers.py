import random
import string

from courier_methods import CourierMethods


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_courier_data():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }


def register_new_courier_and_return_login_password():
    courier_data = generate_courier_data()
    response = CourierMethods.create_courier(courier_data)

    if response.status_code == 201:
        return [courier_data["login"], courier_data["password"], courier_data["firstName"]]
    return []

def generate_login_data():
    courier = generate_courier_data()
    return {"login": courier["login"], "password": courier["password"]}