import requests

from configuration import URL_SERVICE


class CourierMethods:

    @staticmethod
    def create_courier(payload):
        return requests.post(f"{URL_SERVICE}/api/v1/courier", json=payload)

    @staticmethod
    def login_courier(payload):
        return requests.post(f"{URL_SERVICE}/api/v1/courier/login", json=payload)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f"{URL_SERVICE}/api/v1/courier/{courier_id}")